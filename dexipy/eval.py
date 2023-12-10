"""
The module ``dexipy.eval`` implements classess and functions for the evaluation of decision alternatives.
"""

from typing import Any, List, Dict, Optional
from copy import copy, deepcopy
from dexipy.types import CallableOperator, CallableNorm, DexiValue, DexiAlternative, DexiAlternatives, DexiAltData, DexiValueType
import dexipy.utils as utl
import dexipy.values as vls
from dexipy.dexi import  DexiModel, DexiAttribute, DexiScale, DexiFunction, DexiDiscretizeFunction
from dexipy.dexi import  scale_value, bounded_scale_value, att_names

def evaluation_order(att: DexiAttribute, prune: List[str] = []) -> List[str]:
    """Determine the evaluation order of attributes. Interpreted as a sequence,
    the order guarantees that whenever some attribute is reached as a next candidate for
    evaluation, all the affecting attributes have already been evaluated.

    Args:
        att (DexiAttribute): The starting point of evaluation.
        prune (List[str], optional): A list of attribute IDs at which to prune the evaluatiuon.
            The evaluation will treat them as if they were basic attributes, not looking to
            any descendant attributes. Defaults to [].

    Returns:
        List[str]: A list of attrribute IDs in the evaluation order.
    """
    result: List[str] = []

    def add_to_order(att: DexiAttribute) -> None:
        id = att.id
        if not id in result:
            if not id in prune:
                if att.link is not None:
                    add_to_order(att.link)
                else:
                    for inp in att.inputs:
                        add_to_order(inp)
            result.append(id)

    add_to_order(att)
    return result

class DexiEvalParameters:
    """A class defining evaluation parameters.

     Please see :ref:`evaluation` for more information about the evaluation process
     and evaluation methods used in DEXiPy.

    Args:
        method (str): Method name. One of the strings "set", "prob", "fuzzy", "fuzzynorm".
        and_op (CallableOperator): Conjunctive aggregation function.
        or_op (CallableOperator): Disjunctive aggregation function.
        norm (CallableNorm): Normalization function.
    """
    def __init__(self, method: str, and_op: CallableOperator, or_op: CallableOperator, norm: CallableNorm):
        self.method = method
        self.and_op = and_op
        self.or_op = or_op
        self.norm = norm

class DexiEvalMethods:
    """A class defining default :py:class:`dexipy.eval.DexiEvalParameters`
   for the evaluation methods implemented in DEXiPy.

    The default parameters are set as follows::

        import dexipy.utils as utl
        self.set_method(DexiEvalParameters("set", lambda x: 0, lambda x: 1, utl.norm_none))
        self.set_method(DexiEvalParameters("prob", utl.prod, sum, utl.norm_sum))
        self.set_method(DexiEvalParameters("fuzzy", min, max, utl.norm_none))
        self.set_method(DexiEvalParameters("fuzzynorm", min, max, utl.norm_max))
   """

    _eval_methods: Dict[str, DexiEvalParameters] = {}

    def __init__(self):
        self.set_method(DexiEvalParameters("set", lambda x: 0, lambda x: 1, utl.norm_none))
        self.set_method(DexiEvalParameters("prob", utl.prod, sum, utl.norm_sum))
        self.set_method(DexiEvalParameters("fuzzy", min, max, utl.norm_none))
        self.set_method(DexiEvalParameters("fuzzynorm", min, max, utl.norm_max))

    @classmethod
    def set_method(cls, method: DexiEvalParameters) -> None:
        """Sets default evaluation parameters for ``method``.

        Args:
            method (DexiEvalParameters): Evaluation parameters with defined
                method name ``method.method``.
        """
        cls._eval_methods[method.method] = method

    @classmethod
    def get_method(cls, method: str) -> DexiEvalParameters:
        """Gets default evaluation parameters for ``method``.

        Args:
            method (str): Method name.

        Raises:
            ValueError: When method parameters have not been previously defined for the given method name.

        Returns:
            DexiEvalParameters: Default parameters of the given method.
        """
        if not method in cls._eval_methods:
            raise ValueError(f'Unknown evaluation method name: "{method}"' )
        return cls._eval_methods[method]

EvalMethods = DexiEvalMethods()
"""A :py:class:`dexipy.eval.DexiEvalMethods` object containing default
evaluation parameters for all methods implemented in DEXiPy."""

def eval_parameters(method: str,
                   and_op: Optional[CallableOperator] = None,
                   or_op: Optional[CallableOperator] = None,
                   norm: Optional[CallableNorm] = None) -> DexiEvalParameters:
    """Fetches default evaluation parameters from ``EvalMethods`` and
    optionally modifies them considering non-None arguments of this function.

    Args:
        method (str): Method name. Required.
        and_op (Optional[CallableOperator], optional): If not None, set the
            conjuntive aggregation function. Defaults to None.
        or_op (Optional[CallableOperator], optional): If not None, set the
            disjuntive aggregation function. Defaults to None.
        norm (Optional[CallableNorm], optional): If not None, set the normalization function.
            Defaults to None.

    Returns:
        DexiEvalParameters: Fetched and optionally modified evaluation parameters.
    """
    result = copy(EvalMethods.get_method(method))
    if and_op is not None:
        result.and_op = and_op
    if or_op is not None:
        result.or_op = or_op
    if norm is not None:
        result.norm = norm
    return result

def get_alt_value(alt: Any, id: str) -> DexiValue:
    """Returns ``alt[id]``.

    Args:
        alt (Any): Expected a DexiAlternative.
        id (str): Value ID, a key in the ``alt`` dictionary.

    Returns:
        DexiValue: Alternative value corresponding to ID, or None if not found.
    """
    try:
        return alt[id]
    except:
        return None

def evaluate_as_set(funct: DexiFunction, inp_values: List[DexiValue]) -> DexiValue:
    inp_vals = tuple(vls.dexi_value_as_set(val) for val in inp_values)
    if None in inp_vals or set() in inp_vals:
        return None
    inp_args = utl.cartesian_product(*inp_vals)
    result = set()
    for args in inp_args:
        eval = funct.evaluate(args)
        if eval is None:
            return None
        eval = vls.dexi_value_as_set(eval)
        if eval is None:
            return None
        result.update(eval)
    if result == set():
        return None
    return result

def evaluate_as_distribution(funct: DexiFunction, inp_values: List[DexiValue], eval_param: DexiEvalParameters) -> DexiValue:
    inp_distrs = tuple(vls.dexi_value_as_distr(val) for val in inp_values)
    if None in inp_distrs or [] in inp_distrs:
        return None
    args_mem = utl.cartesian_product(*inp_distrs)
    args_idx = utl.cartesian_product(*(tuple(range(utl.objlen(distr))) for distr in inp_distrs))
    ands = [eval_param.and_op(mem) for mem in args_mem]
    assert len(args_mem) == len(args_idx) == len(ands)
    result: List[float] = []
    if funct.attribute is not None and funct.attribute.scale is not None:
        result = [0.0] * funct.attribute.scale.count()
    for idx, mem in enumerate(args_mem):
        if ands[idx] == 0:
            continue
        args = args_idx[idx]
        eval = funct.evaluate(args)
        if eval is None:
            return None
        as_set = vls.dexi_value_as_set(eval)
        nval = utl.objlen(as_set)
        if  nval == 0:
            return None
        as_distr = vls.dexi_value_as_distr(eval)
        as_distr = eval_param.norm(as_distr)
        for i, el in enumerate(as_distr):
            if i >= len(result):
                result = utl.pad_list(result, i + 1, 0.0)
            result[i] = eval_param.or_op([result[i], eval_param.and_op([ands[idx], el])])
    return result

def evaluate_aggregate(att: DexiAttribute, scl: DexiScale, alt: DexiAlternative, eval_param: DexiEvalParameters) -> DexiValue:
    funct = att.funct
    if funct is None:
        return None
    inputs = att.inputs
    inp_ids = att_names(inputs)

    inp_values = [get_alt_value(alt, id) for id in inp_ids]
    if None in inp_values:
        return None
    inp_types = [vls.dexi_value_type(val) for val in inp_values]
    if DexiValueType.none in inp_types or None in inp_types:
        return None

    if isinstance(funct, DexiDiscretizeFunction):
        value = funct.evaluate(inp_values[0])
    elif eval_param.method == "set":
        multi_valued = any(inp != DexiValueType.int for inp in inp_types)
        if multi_valued:
            value = evaluate_as_set(funct, inp_values)
        else:
            value = funct.evaluate(inp_values)
    else:
        value = evaluate_as_distribution(funct, inp_values, eval_param)
    return value

def evaluate(model: DexiModel,
            alternatives: Optional[DexiAltData] = None,
            method: str = "set",
            root: Optional[DexiAttribute] = None,
            prune: List[str] = [],
            pre_check: bool = False,
            bounding: bool = False,
            in_place: bool = False,
            eval_param: Optional[DexiEvalParameters] = None
            ) -> DexiAltData:
    """
    This is the main implementation of the evaluation method in DEXiPy.

    While it is possible to call this function directly, it is also possible to
    avoid importing :py:mod:`dexipy.eval` and run evaluations using
    :py:func:`dexipy.dexi.evaluate` or :py:meth:`dexipy.dexi.DexiModel.evaluate`.

    Please see :ref:`evaluation` for more information about the evaluation process
    and evaluation methods used in DEXiPy.

    Args:
        model (DexiModel): A DexiModel. Required.
        alternatives (Optional[DexiAltData], optional): A single DexiAlternative or a list
            of alternatives (DexiAlternatives). Defaults to None, which selects ``model.alternatives``.
        method (str, optional): One of the strings "set", "prob", "fuzzy", "fuzzynorm" that select
            the evaluation method. Defaults to "set".
        root (Optional[DexiAttribute], optional): The topmost (root) attribute of the evaluation.
            Defaults to None, which selects ``model.root``.
        prune (List[str], optional): List of attribute IDs at which the evaluation is "pruned".
            This means that input attributes below some pruned attribute are not evaluated
            and the pruned attribute is treated as an input (basic) attribute for this evaluation.
            Defaults to [].
        pre_check (bool, optional): Whether of not ``alternatives`` are checked by
            :py:meth:`dexipy,dexi.DexiModel.check_alternatives` prior to evaluation.
            Defaults to False.
        bounding (bool, optional): Whether or not the evaluation keeps calculated values within
            bounds prescribed by the corresponding scales. Defaults to False.
        in_place (bool, optional): If True, evaluation modifies ``alternatives`` in place,
            otherwise a deep copy is made and returned by the method. Defaults to False.
        eval_param (Optional[eval.DexiEvalParameters], optional): Optional
            :py:class:`dexipy.eval.DexiEvalParameters`, which may customize the normalization
            and aggregation methods used in the evaluation. Defaults to None.

    Returns:
        DexiAltData: Returns an evaluated alternative or a list of alternatives,
        depending on the type of the ``alternatives`` argument.
    """
    if eval_param is None:
        eval_param = EvalMethods.get_method(method)
    if alternatives is None:
        alternatives = model.alternatives
    if not in_place:
        alternatives = deepcopy(alternatives)
    listargs = isinstance(alternatives, list)
    alts: DexiAlternatives = alternatives if listargs else [alternatives] # type: ignore

    if root is None:
        root = model.root
    if root is None:
        raise ValueError("Undefined model root")

    pruning = len(prune) > 0
    full_order = evaluation_order(root)
    eval_order = full_order
    if pruning:
        eval_order = evaluation_order(root, prune)
        diff = set(full_order).difference(set(eval_order))
        for id in model.non_root_ids:
            if id in diff:
                for alt in alts:
                    alt[id] = None

    if pre_check:
        check = model.check_alternatives(alts)
        if check["errors"] != []:
            raise ValueError(utl.check_str(check, warnings = True))

    for alt in alts:
        for id in eval_order:
            if id == root.id:
                continue
            att = model.attrib(id)
            if att is None:
                continue
            scl = att.scale
            if scl is None:
                value = None
            elif att.link is not None:
                value = get_alt_value(alt, att.link.id)
            elif att.is_basic() or id in prune:
                value = scale_value(get_alt_value(alt, id), scl)
            elif att.is_aggregate():
                value = evaluate_aggregate(att, scl, alt, eval_param)
            else:
                value = None
            if bounding:
                value = bounded_scale_value(value, scl)
            if eval_param.method != "set" and isinstance(value, list):
                value = eval_param.norm(value)
            value = vls.reduce_dexi_value(value)
            alt[id] = value

    if listargs:
        return alts
    else:
        return alts[0]

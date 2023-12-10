"""
Module ``dexipy.utils`` contains a collection of helper functions used in DEXiPy.
"""

from typing import Any, Union, Tuple, Set, List, Dict, Optional, Iterable
from sys import float_info
import itertools
from dexipy.types import BoundAssoc

def objlen(obj: Any) -> int:
    """Returns length of any object type.

    Args:
        obj (Any): An object.

    Returns:
        int: ``len(obj)`` if object's length is defined, or 0 otherwise.
    """
    try:
        return len(obj)
    except:
        return 0

def table_lines(columns: List[List[str]], align: str = "", def_align: str = "l") -> List[str]:
    """A general-purpose function for making a table from a list of column strings.

    Args:
        columns (List[List[str]]): A list of columns. Each column is a list of strings.
        align (str, optional): A string consisting of letters in ``("l", "c", "r")`` that indicate
            the justification of the corresponding columns . Defaults to "".
        def_align (str, optional): Default aligning character for columns not specified in
            ``align``. Defaults to ``"l"``.

    Returns:
        List[str]: A list of table lines that can be joined for printing.
    """
    result: List[str] = []
    ncol = len(columns)
    acol = pad_list(list(align), ncol, def_align)
    nlin = max(len(col) for col in columns)
    widths = [col_width(col) for col in columns]
    for i in range(nlin):
        line = " ".join(aligned(col[i] if 0 <= i < len(col) else "", widths[c], acol[c]) for c, col in enumerate(columns))
        result.append(line)
    return result

def round_float(val: float, decimals: Optional[int] = None) -> float:
    """Rounds a float number to the required number of decimals.

    Args:
        val (float): An int or float number.
        decimals (Optional[int], optional): The required number of decimals.
            No rounding takes place if None. Defaults to None.

    Raises:
        ValueError: If the ``val`` argument is not an integer or float.

    Returns:
        float: Rounded float value.
    """
    if isinstance(val, int):
        return val
    if isinstance(val, float):
        return val if decimals is None else round(val, decimals)
    raise ValueError(f"Value {val} is not int or float")

def round_float_list(values: List[float], decimals: Optional[int] = None) -> List[float]:
    """Rounds all list elements to the required number of decimals.
    A vectorised version of :py:func:`dexipy.util.round_float`.

    Args:
        values (List[float]): List of floats.
        decimals (Optional[int], optional): The required number of decimals.
            No rounding takes place if None. Defaults to None.

    Returns:
        List[float]: A list of rounded values.
    """
    if decimals:
        return [round(val, decimals) for val in values]
    else:
        return values

def rule_values(vals: str, add: int = 0) -> Tuple[int, ...]:
    """Convert a DEXi rule values string to a tuple of integers to be used in DEXiPy.

    In ``.dxi`` files, values of decision rules are encoded using character strings, where each
    individual character encodes some function value. The encoding is zero-based, so that the character
    ``"0"`` represents the lowest ordinal number on the corresponding discrete scale.

    Args:
        vals (str): A value string as used in ``.dxi`` files.
        add (int, optional): An optional integer value to be added to elements of the resulting tuple.
            Defaults to 0.

    Returns:
        Tuple[int, ...]: A tuple of integers, of the same length as ``vals``.

    Example:
       >>> rule_values("05A")
       (0, 5, 17)
    """
    return tuple((ord(ch) - ord("0") + add) for ch in vals)

def values_to_str(vals: Iterable[int], add: int = 0) -> str:
    """Converts numbers to a DEXi string. A reverse operation of :py:func:`rule_values`.

    Args:
        vals (Iterable[int]): An iterable of integers to be converted to characters.
        add (int, optional): An optional integer value to be added to ``vals`` before
            conversion. Defaults to 0.

    Returns:
        str: A string of the same length as ``vals``.

    Example:
        >>> values_to_str((0, 5, 17))
        '05A'
    """
    return "".join((chr(val + ord("0") + add)) for val in vals)

def set_to_distr(valset: Union[int, Set[int]], length: int = 0) -> Optional[List[float]]:
    """Converts a set to a value distribution.

    Args:
        valset (Union[int, Set[int]]): A value to be converted.
        length (int, optional): The required length of the distribution. Defaults to 0.

    Returns:
        Optional[List[float]]: Set converted to a list of floats.
        The minimal length of the list is ``length``, but it may be extended if ``valset``
        contains elements larger than ``length - 1``.

    Examples:
       >>> set_to_distr(1)
       [0.0, 1.0]
       >>> set_to_distr(1, 5)
       [0.0, 1.0, 0.0, 0.0, 0.0]
       >>> set_to_distr({1,2}, 4)
       [0.0, 1.0, 1.0, 0.0]
    """
    if isinstance(valset, int):
        valset = {valset}
    if len(valset) == 0:
        return length * [0.0]
    elif all([isinstance(val, int) for val in valset]):
        dlen = max(length, max(valset) + 1)
        result = dlen * [0.0]
        for el in valset:
            if el >= 0:
                result[el] = 1.0
        return result
    else:
        return None

def distr_to_set(distr: List[float], eps: float = float_info.epsilon) -> Set[int]:
    """Converts a DEXi value distribution to a DEXi value set.

    Args:
        distr (List[float]): A distribution to be converted.
        eps (float, optional): Threshold for determining whether a distribution element
            can be considered a member of the resulting set. Defaults to float_info.epsilon.

    Returns:
        Set[int]: The set, composed of indices of ``distr`` elements greater than ``eps``.

    Examples:
       >>> distr_to_set([0.0, 0.5, 1.0, 0.0])
       {1, 2}
       >>> distr_to_set([0.0, 0.5, 1.0, 0.0], 0.5)
       {2}
    """
    return {i for i, el in enumerate(distr) if el > eps}

def distr_to_strict_set(distr: List[float], eps: float = float_info.epsilon) -> Optional[Set[int]]:
    """Converts a DEXi value distribution to a DEXi value set.
    Only distributions that strictly represent sets, i.e., they contain only 0.0 and 1.0 entries,
    are converted.

    Args:
        distr (List[float]): A distribution to be converted.
        eps (float, optional): Allowed tolerance around distribution values,
            so that they can be considered 0.0 or 1.0. Defaults to float_info.epsilon.

    Returns:
        Set[int]: The set, composed of indices of ``distr`` elements that differ from 0.0 or 1.0
        for at most ``eps``. None is returned if ``distr`` contains values that are not
        sufficiently close to 0.0 or 1.0.

    Examples:
       >>> distr_to_strict_set([0.0, 0.5, 1.0, 0.0]) # returns None
       >>> distr_to_strict_set([0.0, 1.0, 1.0, 0.0])
       {1, 2}
       >>> distr_to_strict_set([0.0, 0.9, 1.1, 0.0]) # returns None
       >>> distr_to_strict_set([0.0, 0.9, 1.1, 0.0], 0.1)
       {1, 2}
    """
    result = set()
    for i, el in enumerate(distr):
        if 1.0 - eps <= el <= 1.0 + eps:
            result.add(i)
        elif not 0.0 - eps <= el <= 0.0 + eps:
            return None
    return result

def dict_to_list(distr: Dict[int, float]) -> List[float]:
    """Converts a dictionary-form value distribution to a list-form one.
    Example: ``{1: 0.7, 2: 0.2}`` is converted to ``[0.0, 0.7, 0.2]``.

    Args:
        distr (Dict[int, float]): A dictionary-form value distribution to be converted.

    Returns:
        List[float]: A list-form value distribution.

    Examples:
       >>> dict_to_list({1: 0.7, 2: 0.2})
       [0.0, 0.7, 0.2]
    """
    max_val = max(-1, max(distr.keys()))
    result = [0.0] * (max_val + 1)
    for idx, val in distr.items():
        if idx >= 0:
            result[idx] = val
    return result

def norm_sum(vals: List[float], req_sum: float = 1.0) -> List[float]:
    """Normalizes a list of float values so that ``sum(vals) == req_sum``.

    Args:
        vals (List[float]): A list of values.
        req_sum (float, optional): The required sum of the resulting list. Defaults to 1.0.

    Returns:
        List[float]: Normalized list. Returns the original list if ``sum(vals) == 0``.

    Examples:
       >>> norm_sum([0.1, 0.2, 0.5])
       [0.125, 0.25, 0.625]
       >>> norm_sum([0.1, -0.2, 0.5])
       [0.25, -0.5, 1.25]
       >>> norm_sum([0.1, 0.2, 0.5], 2)
       [0.25, 0.5, 1.25]
    """
    try:
        val_sum = sum(vals)
        result = [val * req_sum/val_sum for val in vals]
    except:
        result = vals
    return result

def norm_max(vals: List[float], req_max: float = 1.0) -> List[float]:
    """Normalizes a list of float values so that ``max(values) == req_max``.

    Args:
        vals (List[float]): A list of values.
        req_max (float, optional): The required maximum of the resulting list. Defaults to 1.0.

    Returns:
        List[float]: Normalized list. Returns the original list if ``max(vals) == 0``.

    Examples:
       >>> norm_max([0.1, 0.2, 0.4])
       [0.25, 0.5, 1.0]
       >>> norm_max([0.1, -0.2, 0.4])
       [0.25, -0.5, 1.0]
       >>> norm_max([0.1, -0.2, 0.4], 2)
       [0.5, -1.0, 2.0]
    """
    try:
        val_max = max(vals)
        result = [val * req_max/val_max for val in vals]
    except:
        result = vals
    return result

def norm_none(vals: List[float]) -> List[float]:
    """A no-normalization function that can be used in place of other normalization functions.

    Args:
        vals (List[float]): A list of values.

    Returns:
        List[float]: The original list of values. No normalization is performed.
    """
    return vals

def is_in_range(x: float, lb: float, hb: float,
                la: Optional[BoundAssoc] = BoundAssoc.up, ha: Optional[BoundAssoc] = BoundAssoc.down) -> bool:
    """Checks whether or not the argument ``x`` lies in the interval bounded by ``lb`` and ``hb``,
    considering the corresponding bound associations ``la`` and ``ha``.

    Args:
        x (float): An integer or floating point value.
        lb (float): Lower interval bound.
        hb (float): Upper interval bound.
        la (BoundAssoc, optional): Bound association of ``lb``. Defaults to BoundAssoc.up.
        ha (BoundAssoc, optional): Bound association of ``hb``. Defaults to BoundAssoc.down.

    Returns:
        bool: Whether or not ``x`` lies in the specified interval.

    Examples:
       >>> is_in_range(0.5, 0, 1)
       True
       >>> is_in_range(0.0, 0, 1, BoundAssoc.up, BoundAssoc.down)
       True
       >>> is_in_range(0.0, 0, 1, BoundAssoc.down, BoundAssoc.down)
       False
       >>> is_in_range(1.0, 0, 1, BoundAssoc.down, BoundAssoc.down)
       True
       >>> is_in_range(1.0, 0, 1, BoundAssoc.down, BoundAssoc.up)
       False
    """
    if la is None:
        la = BoundAssoc.up
    if ha is None:
        ha = BoundAssoc.down
    return (lb < x < hb) or (x == lb and la == BoundAssoc.up) or (x == hb and ha == BoundAssoc.down)

def prod(iterable):
    """Calculates the product of arguments.

    Args:
        iterable: A sequence of integer or float numbers.

    Returns:
        int or float: Product of arguments.
    """
    p = 1
    for n in iterable:
        p *= n
    return p

def cartesian_product(*dimensions):
    """Constructs the cartesian product of ranges, tuples or sets submitted as the function arguments.

    Uses :py:func:`itertools.product`.

    Returns:
        List: List of all possible combinations of values of ``dimensions``.

    Examples:
       >>> cartesian_product((0, 1), (2, 3, 4))
       [(0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4)]
       >>> cartesian_product({"a", "b"}, (2, 3, 4))
       [('a', 2), ('a', 3), ('a', 4), ('b', 2), ('b', 3), ('b', 4)]
       >>> cartesian_product(range(2), range(3))
       [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]
    """
    return list(itertools.product(*dimensions))

def unique_names(names: List[str], reserved: List[str] = [], start: int = 0) -> List[str]:
    """Converts a list of strings to a list of unique ID strings.

    Args:
        names (List[str]): A list of strings to be converted to IDs.
        reserved (List[str], optional): Reserved strings that should not be used as IDs.
            Defaults to [].
        start (int, optional): To make IDs unique, indices of the form ``_<int>`` are added
            to the original strings. This argument defines the starting index, which corresponds to the
            first appearance of some string and is incremented before each subsequent occurence.
            Defaults to 0.

    Returns:
        List[str]: A list of unique IDs, of the same length as ``names``.

    Examples:
       >>> unique_names(["name", "state", "name", "city", "name", "zip", "zip"])
       ['name', 'state', 'name_1', 'city', 'name_2', 'zip', 'zip_1']
       >>> unique_names(["name", "state", "name", "city", "name", "zip", "zip"], reserved = ["name"])
       ['name_1', 'state', 'name_2', 'city', 'name_3', 'zip', 'zip_1']
    """
    state = {}
    names = reserved + names
    result = []
    for i, n in enumerate(names):
        if n not in result:
            result.append(n)
            state[n] = start
        else:
            if not n in state:
                state[n] = start
            while True:
                state[n] += 1
                newname = n + "_" + str(state[n])
                if newname not in result:
                    result.append(newname)
                    break
    del result[:len(reserved)]
    return result

def name_to_id(name: str, replace: str = "_") -> str:
    """Replaces all non-alphanumeric characters in ``name`` with ``replace``.

    Args:
        name (str): Some string.
        replace (str, optional): Replacement string. Defaults to "_".

    Returns:
        str: Converted string.

    Example:
       >>> name_to_id("Some #string 1")
       'Some__string_1'
    """
    return "".join([ c if c.isalnum() else replace for c in name ])

def names_to_ids(names: List[str], replace: str = "_") -> List[str]:
    """A vectorised version of :py:func:`dexipy.utils.name_to_id`.

    Args:
        names (List[str]): List of strings.
        replace (str, optional): Replacement string. Defaults to "_".

    Returns:
        List[str]: Converted list of strings, of the same length as ``names``.
    """
    return [name_to_id(name, replace) for name in names]

def pad_list(lst: List[Any], newlen: int, pad: Any) -> List[Any]:
    """Pads a list to the required length, adding ``pad`` elements if necessary.

    Args:
        lst (List[Any]): List of objects of any type.
        newlen (int): The required length of the resulting list.
        pad (Any): Elements to be added if necessary.

    Returns:
        List[Any]: A list obtained from ``lst``, padded to the required length.
    """
    return lst[:newlen] if len(lst) >= newlen else lst + ([pad] * (newlen - len(lst)))

def col_width(column: List[str]) -> int:
    """Calculates the maximum width of strings in ``column``.

    Args:
        column (List[str]): A list of strings.

    Returns:
        int: Maximum string length.
    """
    return max(len(el) for el in column)

def aligned(s: str, width: int = -1, align: str = "l") -> str:
    """Pads and/or aligns the string.

    Args:
        s (str): Some input string.
        width (int, optional): The required length of the resulting string.
            Defaults to -1, not affecting string length.
        align (str, optional): A one-character string in ``("l", "c", "r")``, requesting
            a left, centered or right justification, respectively.

    Returns:
        str: Padded and justified string.
    """
    if width <= 0:
        return s
    if align == "r":
        return s.rjust(width)
    elif align == "l":
        return s.ljust(width)
    elif align == "c":
        return s.center(width)
    else:
        return s

def check_str(check: Dict[str, List[str]], errors: bool = True, warnings: bool = False) -> str:
    """Makes a string, suitable for printing, from an error/warning dictionary.

    Args:
        check (Dict[str, List[str]]): A dictionary in the form ``{"errors": [...], "warnings": [...]}``.
        errors (bool, optional): Should this function consider errors? Defaults to True.
        warnings (bool, optional): Should this function consider warnings? Defaults to False.

    Returns:
        str: A string containing error and warning messages, formatted for printing.
    """
    result = ""
    if errors and check["errors"] != []:
        result = "Errors\n" + "\n".join(check["errors"]) + "\n"
    if warnings and check["warnings"] != []:
        result = result + "Warnings:\n" + "\n".join(check["warnings"]) + "\n"
    return result

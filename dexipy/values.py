"""
Module ``dexipy.values`` contains helper classes and functions for handling DEXi values.
"""

from __future__ import annotations
from typing import Any, Set, List, Optional
from dexipy.types import DexiValue, DexiValueType
import dexipy.utils as utl
import dexipy.dexi as dxi

def dexi_value_type(value: Any) -> Optional[DexiValueType]:
    """Determines the ``DexiValueType`` of the argument.

    Args:
        value (Any): Value object to be checked.

    Returns:
        Optional[DexiValueType]: Enumeration of the argument's DEXi value type.
    """
    if value is None:
        return DexiValueType.none
    val_type = type(value)
    if val_type is int:
        return DexiValueType.int
    if val_type is str:
        return DexiValueType.str
    if val_type is float:
        return DexiValueType.float
    if val_type is set:
        return DexiValueType.set
    if val_type is tuple:
        return DexiValueType.tuple
    if val_type is list:
        return DexiValueType.list
    if val_type is dict:
        return DexiValueType.dict
    return None

def check_dexi_value(value: Any) -> bool:
    """Checks the data object and determines whether or not it represents a ``DexiValue``.

    Only the data structure is checked. Even if the structure is correct, ``value``
    can still contain elements that may not be correct in the context of some specific
    ``DexiScale``. For instance, the object may contain value indices not
    found in the scale definition.

    Args:
        value (Any): Value object to be checked.

    Returns:
        bool: Whether or not the object's structure is valid for representing a ``DexiValue``.
    """
    val_type = dexi_value_type(value)
    if val_type is None:
        return False
    if val_type == DexiValueType.str:
        return value == "*" or value == "" or value.lower().startswith("undef")
    if val_type in (DexiValueType.set, DexiValueType.tuple):
        for val in value:
            if not isinstance(val, int):
                return False
        return True
    if val_type == DexiValueType.list:
        for val in value:
            if not isinstance(val, (int, float)):
                return False
        return True
    if val_type == DexiValueType.dict:
        for key, val in value.items():
            if not (isinstance(key, int) and isinstance(val, (int, float))):
                return False
        return True
    return True

def check_dexi_scale_value(value: Any) -> bool:
    """Checks the data object and determines whether or not it represents a ``DexiScaleValue``.

    Operation is similar to :py:func:`dexipy.values.check_dexi_value`,
    except that it additionally allows using name strings to indicate scale values.

    Only the data structure is checked. Even if the structure is correct, ``value``
    can still contain elements that may not be correct in the context of some specific
    ``DexiScale``. For instance, the object may contain value names or indices not
    found in the scale definition.

    Args:
        value (Any): Value object to be checked.

    Returns:
        bool: Whether or not the object's structure is valid for representing a ``DexiScaleValue``.
    """
    val_type = dexi_value_type(value)
    if val_type is None:
        return False
    if val_type in (DexiValueType.set, DexiValueType.tuple):
        for val in value:
            if not isinstance(val, (int, str)):
                return False
        return True
    if val_type == DexiValueType.list:
        for val in value:
            if not isinstance(val, (int, float)):
                return False
        return True
    if val_type == DexiValueType.dict:
        for key, val in value.items():
            if not (isinstance(key, (int, str)) and isinstance(val, (int, float))):
                return False
        return True
    return True

def dexi_value_as_set(value: DexiValue, strict: bool = False) -> Optional[Set[int]]:
    """Converts a ``DexiValue`` object to a set.

    Args:
        value (DexiValue): A DEXi value object.
        strict (bool, optional): Defines the conversion from value distributions.
           When True, only distributions that clearly represent sets, i.e., contain only
           0.0 or 1.0 elements, are converted. When False, all elements with non-zero values
           are considered set members, too. Defaults to False.

    Returns:
        Optional[Set[int]]: Resulting value set. None if ``value`` cannot be interpreted as a set.

    Examples:
       >>> dexi_value_as_set([0, 1, 0.5, 1], strict = True) # returns None
       >>> dexi_value_as_set([0, 1, 0.0, 1], strict = True)
       {1, 3}
       >>> dexi_value_as_set([0, 1, 0.5, 1], strict = False)
       {1, 2, 3}
    """
    if isinstance(value, int):
        return {value}
    if isinstance(value, (set, tuple)):
        result = set(val if isinstance(val, int) else None for val in value)
        if None in result:
            return None
        else:
            return result
    if isinstance(value, dict):
        value = utl.dict_to_list(value)
    if isinstance(value, list):
        if strict:
            return utl.distr_to_strict_set(value)
        else:
            return utl.distr_to_set(value)
    return None

def dexi_value_as_distr(value: DexiValue) -> Optional[List[float]]:
    """Converts a ``DexiValue`` object to a value distribution.

    Args:
        value (DexiValue): A DEXi value object.

    Returns:
        Optional[List[float]]: ``value`` represented in terms of a value distribution,
        or None if it cannot be interpreted.

    Examples:
       >>> dexi_value_as_distr(2)
       [0.0, 0.0, 1.0]
       >>> dexi_value_as_distr({1, 2})
       [0.0, 1.0, 1.0]
       >>> dexi_value_as_distr({0: 0.5, 2: 1.0})
       [0.5, 0.0, 1.0]
       >>> dexi_value_as_distr((1, 1, 2, 2))
       [0.0, 1.0, 1.0]
    """

    if isinstance(value, int):
        value = {value}
    if isinstance(value, tuple):
        value = set(value)
    if isinstance(value, set):
        return utl.set_to_distr(value)
    if isinstance(value, dict):
        value = utl.dict_to_list(value)
    if isinstance(value, list):
        return value
    return None

def reduce_set(value: Any) -> DexiValue:
    """Reduces a ``DexiValue``, represented as a set, to a smaller data representation,
    if possible

    Typical reductions:
       * an empty set to None: ``{} -> None``
       * a single-element tuple or set to int: ``(1,) -> {1} -> 1`` or ``{"low"} -> "low"``

    Args:
        value (Any): A DEXi value object.

    Returns:
        DexiValue: Reduced representation of ``value``, or ``value`` itself if no reduction is possible.

    Examples:
       >>> reduce_set(set()) # returns None
       >>> reduce_set({1})
       1
       >>> reduce_set({1, 2}) # no reduction
       {1, 2}
       >>> reduce_set(0.1) # no reduction
       0.1
    """
    if not isinstance(value, set):
        return value
    if len(value) == 0:
        return None
    if len(value) == 1:
        (element,) = value
        if isinstance(element, (str, int)):
            return element
    return value

def reduce_dexi_value(value: DexiValue) -> DexiValue:
    """Reduce a ``DexiValue`` to a smaller and possibly more comprehensible data representation,
    if possible.

    Typical reductions:
       * a tuple to set: ``(1, 1, 2, 2) -> {1, 2}``
       * a single-element tuple or set to int: ``(1,) -> {1} -> 1``
       * a distribution to set, if possible: ``[1.0, 0.0, 1.0] -> {0, 2}``

    Args:
        value (DexiValue): A DEXi value object.

    Returns:
        DexiValue: Reduced representation of ``value``, or ``value`` itself
        if no reduction is possible.

    Examples:
       >>> reduce_dexi_value((1, 1, 2, 2))
       {1, 2}
       >>> reduce_dexi_value({1})
       1
       >>> reduce_dexi_value([1.0, 0.0, 1.0])
       {0, 2}
       >>> reduce_dexi_value([1.0, 0.5, 1.0]) # no reduction
       [1.0, 0.5, 1.0]
       >>> reduce_dexi_value({1: 1.0})
       1
    """
    val_type = dexi_value_type(value)
    if val_type in (DexiValueType.set, DexiValueType.tuple):
        return reduce_set(set(value))  # type: ignore
    if val_type == DexiValueType.list:
        as_set = utl.distr_to_strict_set(value) # type: ignore
        if isinstance(as_set, set):
            return reduce_set(as_set)
    if val_type == DexiValueType.dict:
        as_distr = dexi_value_as_distr(value)
        if as_distr is not None:
            return reduce_dexi_value(as_distr)
    return value

class DexiValues:
    """A wrapper class around a ``DexiValue`` data element.
    An object of this class contains a DEXi value :py:attr:`dexipy.values.DexiValues.value`,
    on which methods operate.

    Args:
       value (Any): A ``DexiValue`` object stored internally and operated upon by methods.
    """

    def __init__(self, value: Any):
        """Create a ``DexiValues`` object.

        Args:
            value (Any): A DEXi value to be operated upon.
        """
        self.value = value

    def value_type(self) -> Optional[DexiValueType]:
        """Determine the value type of ``self.value``."""
        return dexi_value_type(self.value)

    def check_value(self) -> bool:
        """Check whether or not ``self.value`` contains valid ``DexiValue`` data."""
        return check_dexi_value(self.value)

    def check_scale_value(self) -> bool:
        """Check whether or not ``self.value`` contains valid ``DexiScaleValue`` data."""
        return check_dexi_scale_value(self.value)

    def as_set(self, strict: bool = False) -> Optional[Set[int]]:
        """Convert ``self.value`` to a set, if possible.
        See :py:meth:`dexipy.values.dexi_value_as_set` for details.

        Args:
            strict (bool, optional): Defines the conversion when ``self.value`` is a value distribution.
               When True, only distributions that clearly represent sets, i.e., contain only
               0.0 or 1.0 elements, are converted. When False, all elements with non-zero values
               are considered set members, too. Defaults to False.
        """
        return dexi_value_as_set(self.value, strict = strict)

    def as_distr(self) -> Optional[List[float]]:
        """Convert ``self.value`` to a value distribution, if possible."""
        return dexi_value_as_distr(self.value)

    def reduce(self) -> DexiValue:
        """Reduces the data representation of ``self.value``, if possible."""
        return reduce_dexi_value(self.value)

    def reduce_value(self) -> None:
        """Returns a reduced data representation of ``self.value``."""
        self.value = reduce_dexi_value(self.value)

    def val_str(self, scale: Any, none: Optional[str] = None,
                reduce: bool = False, decimals: Optional[int] = None, use_dict: bool = True) -> Optional[str]:
        """Returns a string representation of ``self.value``.
        See :py:func:`dexipy.dexi.value_text` for more details.

        Args:
            scale (Any): Expected a :py:class:`dexipy.dexi.DexiScale` object.
            none (Optional[str], optional): An optional string that is returned
                when the value cannot be interpreted. Defaults to None.
            reduce (bool, optional): Whether or not the value is reduced
                (see :py:func:`reduce_dexi_value`) prior to processing. Defaults to False.
            decimals (Optional[int], optional): The number of decimals used to display
                float numbers. Defaults to None.
            use_dict (bool, optional): Whether or not the dictionary-form is used for displaying
                value distributions (rather than list-form). Defaults to True.
        """
        return dxi.value_text(self.value, scale, none = none, reduce = reduce, decimals = decimals, use_dict = use_dict)

"""
Module ``dexipy.types`` defines type aliases and enumeration classess that are used throughout DEXiPy.
"""

from enum import Enum
from typing import  Set, Tuple, List, Dict, Union, Callable

class BoundAssoc(Enum):
    """Enumeration associated with bounds that discretize continuous scales.

    Args:
        Enum (int): indicates the interval to which some corresponding bound :math:`b` belongs.
    """

    down = -1
    """Indicates that :math:`b` belongs to the interval :math:`<= b`."""

    up = 1
    """Indicates that :math:`b` belongs to the interval :math:`b >=`."""


# internal representation of values
DexiValue = Union[None, str, float, Tuple[int], Set[int], List[float], Dict[int, float]]
"""Type alias: Admissible DEXi values that can be interpreted without knowing the ``DexiScale`` context.
"""

# values interpretable on scales
DexiScaleValue = Union[None, str, float, Tuple[Union[int, str]], Set[Union[int, str]], List[float], Dict[Union[int, str], float]]
"""Type alias: Admissible DEXi values that can be interpreted in a given ``DexiScale`` context.
"""

class DexiValueType(Enum):
    """Enumeration of ``DexiValue`` data types."""

    none = 0
    str = 1
    int = 2
    float = 3
    set = 4
    tuple = 5
    list = 6
    dict = 7

DexiAlternative = Dict[Union[str, int], DexiValue]
"""Type alias: Representation of a single decision alternative:
   ``Dict[Union[str, int], DexiValue]``.
"""

DexiAlternatives = List[DexiAlternative]
"""Type alias: Representation of multiple decision alternatives as
   ``List[DexiAlternative]``.
"""

DexiAltData = Union[DexiAlternative, DexiAlternatives]
"""Type alias: General representation of alternatives:
    ``Union[DexiAlternative, DexiAlternatives]``.
"""

CallableNorm = Callable[..., List[float]]
"""Type alias: Callable normalization functions, that accept and return a list of floats."""

CallableOperator = Callable[[List[float]], float]
"""Type alias: Callable ``and_op`` and ``or_op`` operator functions that accept a list of floats and return a single float."""

class DexiOrder(Enum):
    """ Enumeration of ``DexiScale`` preferential order.

    Args:
        Enum (int): Preferential order.
    """
    descending = -1
    """Scale values are ordered from "good" to "bad" ones."""

    none = 0
    """Scale values are not ordered by preference."""

    ascending = 1
    """Scale values are ordered from "bad" to "good" ones (default)."""

class DexiQuality(Enum):
    """Enumeration of ``DexiScale`` scale value quality classes.

    Args:
        Enum (int): Scale value quality class.
    """

    bad = -1
    """A "bad" value class, indicating an undesired value."""

    none = 0
    """A "neutral" value class, neither particularly "good" nor "bad"."""

    good = 1
    """A "good" value class, indicating a highly desired, ideal, value."""

class DexiEvalMethod(Enum):
    """Enumeration od DEXiPy evaluation methods.

    Args:
        Enum (int): Evaluation method.
    """
    set = 1
    """Evaluation using sets (default)."""

    prob = 2
    """Evaluation interpreting DEXi values as probability distributions."""

    fuzzy = 3
    """Evaluation interpreting DEXi values as fuzzy set memberships (possibility distributions)."""

    fuzzynorm = 4
    """Similar to ``fuzzy``, but enforcing fuzzy normalization (the maximum distribution element must equal to 1.0)."""

"""
pyset - library for sorting objects into sets
"""

from .core import PySet, NumberSet, WordSet
from .utils import compare_sets, filter_common

__version__ = "1.0.0"
__all__ = ["PySet", "NumberSet", "WordSet", "compare_sets", "filter_common"]

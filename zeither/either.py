from __future__ import annotations
from typing import Any, Callable, Generic, TypeVar


_Left = TypeVar("_Left", covariant=True)
_Right = TypeVar("_Right", covariant=True)
_Arg1 = TypeVar("_Arg1", covariant=True)
_Result1 = TypeVar("_Result1", covariant=True)


class Either(Generic[_Right, _Left]):
    def __init__(self, value: Any, is_right: bool = True):
        self._value = value
        self._is_right = is_right

    @property
    def value(self) -> Any:
        return self._value

    @property
    def is_right(self) -> bool:
        return self._is_right

    def map(self, function: Callable[[_Arg1], _Result1]) -> Either:
        if self._is_right:
            result = function(self._value)
            return Either(result)
        return Either(self._value, False)

    @staticmethod
    def is_either(o: object):
        if isinstance(o, Either):
            return True
        return False


right: Callable[[Any], Either] = lambda x: Either(x)

left: Callable[[Any], Either] = lambda x: Either(x, False)

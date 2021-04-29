from __future__ import annotations
from typing import Any, Callable, Generic, TypeVar


_Left = TypeVar("_Left", covariant=True)
_Right = TypeVar("_Right", covariant=True)
_Arg1 = TypeVar("_Arg1")
_Result1 = TypeVar("_Result1", covariant=True)
_Value = TypeVar("_Value", covariant=True)


class Either(Generic[_Left, _Right]):
    def __init__(self, value: _Value, is_right: bool = True):
        self._value = value
        self._is_right = is_right

    @property
    def value(self) -> _Value:
        return self._value

    @property
    def is_right(self) -> bool:
        return self._is_right

    def right(self) -> Either[_Left, _Right]:
        if self.is_right:
            return self._value
        raise ValueError("try to extract right value on left")

    def left(self) -> Either[_Left, _Right]:
        if not self.is_right:
            return self._value
        raise ValueError("try to extract left value on right")

    def map(self, function: Callable[[_Arg1], _Result1]) -> Either[_Left, _Result1]:
        if self._is_right:
            result = function(self._value)
            return right(result)
        return left(self._value)

    def left_map(
        self, function: Callable[[_Arg1], _Result1]
    ) -> Either[_Result1, _Right]:
        if self._is_right:
            return right(self._value)
        result = function(self._value)
        return left(result)

    def bind(self, function: Callable[[_Arg1], Either]) -> Either[_Left, _Right]:
        if self._is_right:
            either = function(self._value)
            return either
        return left(self._value)


right: Callable[[_Arg1], Either[_Left, _Right]] = lambda value: Either(value)

left: Callable[[_Arg1], Either[_Left, _Right]] = lambda value: Either(value, False)

is_either: Callable[[_Arg1], bool] = lambda o: isinstance(o, Either)
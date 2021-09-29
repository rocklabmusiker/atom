# --------------------------------------------------------------------------------------
# Copyright (c) 2021, Nucleic Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# --------------------------------------------------------------------------------------
from typing import (
    Any,
    Callable,
    Dict,
    Literal,
    Optional,
    Tuple,
    Type,
    TypeVar,
    overload,
)

from .catom import Member

T = TypeVar("T")
T1 = TypeVar("T1")
T2 = TypeVar("T2")

class Instance(Member[T, T]):
    # Single Type
    @overload
    def __new__(
        cls,
        kind: Type[T],
        args: Optional[tuple] = None,
        kwargs: Optional[Dict[str, Any]] = None,
        *,
        factory: Optional[Callable[[], T]] = None,
        optional: Literal[True] = True,
    ) -> Instance[Optional[T]]: ...
    @overload
    def __new__(
        cls,
        kind: Type[T],
        args: Optional[tuple] = None,
        kwargs: Optional[Dict[str, Any]] = None,
        *,
        factory: Optional[Callable[[], T]] = None,
        optional: Literal[False],
    ) -> Instance[T]: ...
    # 1-tuple
    @overload
    def __new__(
        cls,
        kind: Tuple[Type[T]],
        args: Optional[tuple] = None,
        kwargs: Optional[Dict[str, Any]] = None,
        *,
        factory: Optional[Callable[[], T]] = None,
        optional: Literal[True] = True,
    ) -> Instance[Optional[T]]: ...
    @overload
    def __new__(
        cls,
        kind: Tuple[Type[T]],
        args: Optional[tuple] = None,
        kwargs: Optional[Dict[str, Any]] = None,
        *,
        factory: Optional[Callable[[], T]] = None,
        optional: Literal[False],
    ) -> Instance[T]: ...
    # 2-tuple
    @overload
    def __new__(
        cls,
        kind: Tuple[Type[T], Type[T1]],
        args: Optional[tuple] = None,
        kwargs: Optional[Dict[str, Any]] = None,
        *,
        factory: Optional[
            Callable[[], T] | Callable[[], T1] | Callable[[], T | T1]
        ] = None,
        optional: Literal[True] = True,
    ) -> Instance[Optional[T | T1]]: ...
    @overload
    def __new__(
        cls,
        kind: Tuple[Type[T], Type[T1]],
        args: Optional[tuple] = None,
        kwargs: Optional[Dict[str, Any]] = None,
        *,
        factory: Optional[
            Callable[[], T] | Callable[[], T1] | Callable[[], T | T1]
        ] = None,
        optional: Literal[False],
    ) -> Instance[T | T1]: ...
    # 3-tuple
    @overload
    def __new__(
        cls,
        kind: Tuple[Type[T], Type[T1], Type[T2]],
        args: Optional[tuple] = None,
        kwargs: Optional[Dict[str, Any]] = None,
        *,
        factory: Optional[
            Callable[[], T]
            | Callable[[], T1]
            | Callable[[], T2]
            | Callable[[], T | T1]
            | Callable[[], T | T2]
            | Callable[[], T1 | T2]
            | Callable[[], T | T1 | T2]
        ] = None,
        optional: Literal[True] = True,
    ) -> Instance[Optional[T | T1 | T2]]: ...
    @overload
    def __new__(
        cls,
        kind: Tuple[Type[T], Type[T1], Type[T2]],
        args: Optional[tuple] = None,
        kwargs: Optional[Dict[str, Any]] = None,
        *,
        factory: Optional[
            Callable[[], T]
            | Callable[[], T1]
            | Callable[[], T2]
            | Callable[[], T | T1]
            | Callable[[], T | T2]
            | Callable[[], T1 | T2]
            | Callable[[], T | T1 | T2]
        ] = None,
        optional: Literal[False],
    ) -> Instance[T | T1 | T2]: ...

class ForwardInstance(Member[T, T]):
    # Single Type
    @overload
    def __new__(
        cls,
        kind: Callable[[], Type[T]],
        args: Optional[tuple] = None,
        kwargs: Optional[Dict[str, Any]] = None,
        *,
        factory: Optional[Callable[[], T]] = None,
        optional: Literal[True] = True,
    ) -> ForwardInstance[Optional[T]]: ...
    @overload
    def __new__(
        cls,
        kind: Callable[[], Type[T]],
        args: Optional[tuple] = None,
        kwargs: Optional[Dict[str, Any]] = None,
        *,
        factory: Optional[Callable[[], T]] = None,
        optional: Literal[False],
    ) -> ForwardInstance[T]: ...
    # 1-tuple
    @overload
    def __new__(
        cls,
        kind: Callable[[], Tuple[Type[T]]],
        args: Optional[tuple] = None,
        kwargs: Optional[Dict[str, Any]] = None,
        *,
        factory: Optional[Callable[[], T]] = None,
        optional: Literal[True] = True,
    ) -> ForwardInstance[Optional[T]]: ...
    @overload
    def __new__(
        cls,
        kind: Callable[[], Tuple[Type[T]]],
        args: Optional[tuple] = None,
        kwargs: Optional[Dict[str, Any]] = None,
        *,
        factory: Optional[Callable[[], T]] = None,
        optional: Literal[False],
    ) -> ForwardInstance[T]: ...
    # 2-tuple
    @overload
    def __new__(
        cls,
        kind: Callable[[], Tuple[Type[T], Type[T1]]],
        args: Optional[tuple] = None,
        kwargs: Optional[Dict[str, Any]] = None,
        *,
        factory: Optional[
            Callable[[], T] | Callable[[], T1] | Callable[[], T | T1]
        ] = None,
        optional: Literal[True] = True,
    ) -> ForwardInstance[Optional[T | T1]]: ...
    @overload
    def __new__(
        cls,
        kind: Callable[[], Tuple[Type[T], Type[T1]]],
        args: Optional[tuple] = None,
        kwargs: Optional[Dict[str, Any]] = None,
        *,
        factory: Optional[
            Callable[[], T] | Callable[[], T1] | Callable[[], T | T1]
        ] = None,
        optional: Literal[False],
    ) -> ForwardInstance[T | T1]: ...
    # 3-tuple
    @overload
    def __new__(
        cls,
        kind: Callable[[], Tuple[Type[T], Type[T1], Type[T2]]],
        args: Optional[tuple] = None,
        kwargs: Optional[Dict[str, Any]] = None,
        *,
        factory: Optional[
            Callable[[], T]
            | Callable[[], T1]
            | Callable[[], T2]
            | Callable[[], T | T1]
            | Callable[[], T | T2]
            | Callable[[], T1 | T2]
            | Callable[[], T | T1 | T2]
        ] = None,
        optional: Literal[True] = True,
    ) -> ForwardInstance[Optional[T | T1 | T2]]: ...
    @overload
    def __new__(
        cls,
        kind: Callable[[], Tuple[Type[T], Type[T1], Type[T2]]],
        args: Optional[tuple] = None,
        kwargs: Optional[Dict[str, Any]] = None,
        *,
        factory: Optional[
            Callable[[], T]
            | Callable[[], T1]
            | Callable[[], T2]
            | Callable[[], T | T1]
            | Callable[[], T | T2]
            | Callable[[], T1 | T2]
            | Callable[[], T | T1 | T2]
        ] = None,
        optional: Literal[False],
    ) -> ForwardInstance[T | T1 | T2]: ...
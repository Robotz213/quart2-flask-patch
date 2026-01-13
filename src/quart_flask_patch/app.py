# The aim is to replace the Quart class exception handling defaults to
# allow for Werkzeug HTTPExceptions to be considered in a special way
# (like the quart HTTPException). In addition a Flask reference is
# created.
from __future__ import annotations

from functools import wraps
from inspect import iscoroutine, iscoroutinefunction
from typing import Any, Awaitable, Callable

from quart.app import Quart

from ._synchronise import sync_with_context


def new_ensure_async(  # type: ignore
    self, func: Callable[..., Any]
) -> Callable[..., Awaitable[Any]]:
    if iscoroutinefunction(func):
        return func
    else:

        @wraps(func)
        async def _wrapper(*args: Any, **kwargs: Any) -> Any:
            result = func(*args, **kwargs)
            if iscoroutine(result):
                return await result
            else:
                return result

        return _wrapper


Quart.ensure_async = new_ensure_async  # type: ignore


def ensure_sync(self, func: Callable) -> Callable:  # type: ignore
    if iscoroutinefunction(func):

        @wraps(func)
        def _wrapper(*args: Any, **kwargs: Any) -> Any:
            return sync_with_context(func(*args, **kwargs))

        return _wrapper
    else:
        return func


Quart.ensure_sync = ensure_sync  # type: ignore

Flask = Quart

__all__ = ("Quart",)

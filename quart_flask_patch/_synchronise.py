# pyright: basic
# pyright: reportPrivateUsage=false
# pyright: reportAttributeAccessIssue=false

from __future__ import annotations

from collections.abc import Awaitable
from typing import TYPE_CHECKING

import greenback
import quart.globals as quart_globals

if TYPE_CHECKING:
    from _typeshed import Incomplete as Any


def _copy_context() -> Any:
    for context_name in ("_cv_request", "_cv_websocket", "_cv_app"):
        context_var = getattr(quart_globals, context_name, None)
        if context_var is not None:
            context = context_var.get(None)
            if context is not None:
                return context.copy()
    return None


def sync_with_context(future: Awaitable[Any]) -> Any:
    context = _copy_context()

    async def context_wrapper() -> Any:
        if context is not None:
            async with context:
                return await future
        else:
            return await future

    return greenback.await_(context_wrapper())

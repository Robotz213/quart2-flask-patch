# pyright: basic
# pyright: reportPrivateUsage=false
# pyright: reportAttributeAccessIssue=false

from __future__ import annotations

from typing import TYPE_CHECKING

import quart
from quart import globals as quart_globals
from quart.globals import _cv_app, app_ctx, current_app, g
from quart.globals import request as quart_request
from quart.globals import session as quart_session
from werkzeug.datastructures import MultiDict
from werkzeug.local import LocalProxy

from ._synchronise import sync_with_context

if TYPE_CHECKING:
    from _typeshed import Incomplete as Any


class FlaskRequestProxy[KT, VT](LocalProxy[KT]):
    @property
    def data(self) -> bytes:
        return sync_with_context(self._get_current_object().data)

    @property
    def form(self) -> MultiDict[Any, Any]:
        return sync_with_context(self._get_current_object().form)

    @property
    def files(self) -> MultiDict[Any, Any]:
        return sync_with_context(self._get_current_object().files)

    @property
    def values(self) -> MultiDict[Any, Any]:
        return sync_with_context(self._get_current_object().values)

    @property
    def json(self) -> Any:
        return sync_with_context(self._get_current_object().json)

    def get_json(self, *args: Any, **kwargs: Any) -> Any:
        return sync_with_context(self._get_current_object().get_json(*args, **kwargs))

    def get_data(self, *args: Any, **kwargs: Any) -> str | bytes:
        return sync_with_context(self._get_current_object().get_data(*args, **kwargs))


def _get_request() -> Any:
    context = _cv_app.get(None)
    if context is not None and getattr(context, "has_request", False):
        return context.request
    return quart_request


def _get_session() -> Any:
    context = _cv_app.get(None)
    if context is not None and getattr(context, "has_request", False):
        return context.session
    return quart_session


request = FlaskRequestProxy(_get_request)
session = LocalProxy(_get_session)

quart_globals.request = request
quart_globals.session = session
quart.request = request
quart.session = session

for _name in ("_cv_request", "_cv_websocket", "request_ctx"):
    if hasattr(quart_globals, _name):
        globals()[_name] = getattr(quart_globals, _name)

__all__ = (
    "_cv_app",
    "app_ctx",
    "current_app",
    "g",
    "request",
    "session",
) + tuple(
    name
    for name in ("_cv_request", "_cv_websocket", "request_ctx")
    if hasattr(quart_globals, name)
)  # pyright: ignore[reportUnsupportedDunderAll]

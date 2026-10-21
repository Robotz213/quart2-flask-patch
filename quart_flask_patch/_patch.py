from __future__ import annotations

import inspect
import sys
import types
from typing import Any, Callable

from ._synchronise import sync_with_context


def _context_decorator(func: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        return sync_with_context(func(*args, **kwargs))

    return wrapper


def _convert_module(new_name, module):  # type: ignore
    new_module = types.ModuleType(new_name)
    for name, member in inspect.getmembers(module):
        if inspect.getmodule(member) == module and inspect.iscoroutinefunction(member):
            setattr(new_module, name, _context_decorator(member))
        else:
            setattr(new_module, name, member)
    setattr(new_module, "_QUART_PATCHED", True)
    return new_module


def _patch_modules() -> None:
    # Create a set of Flask modules, prioritising those within the
    # flask_patch namespace over simple references to the Quart
    # versions.
    flask_modules = {}
    for name, module in list(sys.modules.items()):
        if name.startswith("quart_flask_patch._"):
            continue
        elif name.startswith("quart_flask_patch"):
            setattr(module, "_QUART_PATCHED", True)
            flask_modules[name.replace("quart_flask_patch", "flask")] = module

    sys.modules.update(flask_modules)


def patch_all() -> None:
    _patch_modules()

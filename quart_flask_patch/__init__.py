# pyright: basic
from __future__ import annotations  # isort:skip

import quart  # isort:skip
import quart_flask_patch.app  # isort:skip
import quart_flask_patch.cli  # isort:skip
import quart_flask_patch.globals  # isort:skip
import quart_flask_patch.helpers  # isort:skip
import quart_flask_patch.testing  # isort:skip # noqa: F401
import quart.views  # isort:skip # noqa: F401
from quart_flask_patch._patch import patch_all  # isort:skip

patch_all()

from flask.app import Flask
from flask.blueprints import Blueprint
from flask.config import Config
from flask.ctx import (
    after_this_request,
    copy_current_request_context,
    has_app_context,
    has_request_context,
)
from flask.globals import current_app, g, request, session
from flask.helpers import (
    flash,
    get_flashed_messages,
    get_template_attribute,
    make_response,
    send_file,
    send_from_directory,
    stream_with_context,
    url_for,
)
from flask.json import jsonify
from flask.signals import (
    appcontext_popped,
    appcontext_pushed,
    appcontext_tearing_down,
    before_render_template,
    got_request_exception,
    message_flashed,
    request_finished,
    request_started,
    request_tearing_down,
    template_rendered,
)
from flask.templating import render_template, render_template_string
from flask.typing import ResponseReturnValue
from flask.wrappers import Request, Response
from markupsafe import Markup, escape
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

__all__ = (
    "Blueprint",
    "Config",
    "Flask",
    "Markup",
    "Request",
    "Response",
    "ResponseReturnValue",
    "abort",
    "after_this_request",
    "appcontext_popped",
    "appcontext_pushed",
    "appcontext_tearing_down",
    "before_render_template",
    "copy_current_request_context",
    "current_app",
    "escape",
    "flash",
    "g",
    "get_flashed_messages",
    "get_template_attribute",
    "got_request_exception",
    "has_app_context",
    "has_request_context",
    "jsonify",
    "make_response",
    "message_flashed",
    "redirect",
    "render_template",
    "render_template_string",
    "request",
    "request_finished",
    "request_started",
    "request_tearing_down",
    "send_file",
    "send_from_directory",
    "session",
    "stream_with_context",
    "template_rendered",
    "url_for",
)


import sys  # isort:skip

json = sys.modules["flask.json"]
sys.modules["flask"] = sys.modules[__name__]

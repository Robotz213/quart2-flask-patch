# pyright: basic
# pyright: reportPrivateUsage=false
# pyright: reportAttributeAccessIssue=false
# pyright: reportPrivateImportUsage=false

from __future__ import annotations

from quart.cli import (  # noqa: F401
    AppGroup,
    QuartGroup,
    ScriptInfo,
    click,
    run_command,
    shell_command,
    with_appcontext,
)

FlaskGroup = QuartGroup

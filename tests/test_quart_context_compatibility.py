import quart_flask_patch  # noqa: F401
from quart import Quart, request, session

app = Quart(__name__)
app.secret_key = "secret"


@app.route("/", methods=["POST"])
async def index() -> str:
    session["method"] = request.method
    return session["method"]


@app.route("/json", methods=["POST"])
async def json_index() -> dict[str, bool]:
    return request.get_json(force=True)


async def test_unified_request_context() -> None:
    response = await app.test_client().post("/")

    assert response.status_code == 200
    assert await response.get_data(as_text=True) == "POST"


async def test_request_get_json_from_async_handler() -> None:
    response = await app.test_client().post("/json", json={"ok": True})

    assert response.status_code == 200
    assert await response.get_json() == {"ok": True}

import quart_flask_patch  # noqa: F401
from quart import Quart, request, session

app = Quart(__name__)
app.secret_key = "secret"


@app.route("/", methods=["POST"])
async def index() -> str:
    session["method"] = request.method
    return session["method"]


async def test_unified_request_context() -> None:
    response = await app.test_client().post("/")

    assert response.status_code == 200
    assert await response.get_data(as_text=True) == "POST"

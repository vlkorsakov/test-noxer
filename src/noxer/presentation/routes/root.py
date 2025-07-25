from flask import Blueprint, Response, jsonify

blueprint = Blueprint("root", __name__)


@blueprint.route("/")
def process_root() -> Response:
    return jsonify(
        {
            "ok": True,
        }
    )

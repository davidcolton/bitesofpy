from flask import Flask, jsonify, abort, request

app = Flask(__name__)

quotes = [
    {
        "id": 1,
        "quote": "I'm gonna make him an offer he can't refuse.",
        "movie": "The Godfather",
    },
    {"id": 2, "quote": "Get to the choppa!", "movie": "Predator"},
    {
        "id": 3,
        "quote": "Nobody's gonna hurt anybody. We're gonna be like three little Fonzies here.",  # noqa E501
        "movie": "Pulp Fiction",
    },
]


def _get_quote(qid):
    """Recommended helper"""
    return [q for q in quotes if qid == q["id"]]


def _quote_exists(existing_quote):
    """Recommended helper"""
    return [q for q in quotes if q["quote"] == existing_quote]


@app.route("/api/quotes", methods=["GET"])
def get_quotes():
    return jsonify({"quotes": quotes})


@app.route("/api/quotes/<int:qid>", methods=["GET"])
def get_quote(qid):
    q = _get_quote(qid)
    if not q:
        abort(404)

    return jsonify({"quotes": q})


@app.route("/api/quotes", methods=["POST"])
def create_quote():
    if not request.json:
        abort(400)
    q = request.json.get("quote")
    m = request.json.get("movie")
    if not q or not m or _quote_exists(q):
        abort(400)

    next_id = max([q["id"] for q in quotes]) + 1
    new_quote = {"id": next_id, "quote": q, "movie": m}
    quotes.append(new_quote)
    return jsonify({"quote": new_quote}), 201


@app.route("/api/quotes/<int:qid>", methods=["PUT"])
def update_quote(qid):
    if not request.json:
        abort(400)
    elif len(_get_quote(qid)) != 1:
        abort(404)

    q = request.json.get("quote")
    m = request.json.get("movie")

    for q_id in [q["id"] for q in quotes]:
        if qid == quotes[q_id]["id"]:
            if quotes[q_id]["quote"] == q and quotes[q_id]["movie"] == m:
                return jsonify({"quote": quotes[q_id]}), 200
            else:
                quotes[q_id]["quote"] = q
                quotes[q_id]["movie"] = m
                return jsonify({"quote": quotes[q_id]}), 200


@app.route("/api/quotes/<int:qid>", methods=["DELETE"])
def delete_quote(qid):
    if len(_get_quote(qid)) == 1:
        for q_id in [q["id"] for q in quotes]:
            if quotes[q_id]["id"] == qid:
                del quotes[q_id]
                return "", 204
    abort(404)

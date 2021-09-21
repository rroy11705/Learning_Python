from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

income = [
    {
        "description": "salary",
        "amount": 5000
    }
]

stock = {
    "fruit": {
        "apple": 100,
        "banana": 84,
        "cherry": 1000
    }
}


@app.route("/incomes")
def get_income():
    return jsonify(income)


@app.route("/incomes", methods=["POST"])
def add_income():
    income.append(request.get_json())
    return "Created", 201


@app.route("/stock")
def get_stock():
    res = make_response(jsonify(stock), 200)
    return res


@app.route("/stock/<collection>")
def get_collection(collection):
    if collection in stock:
        res = make_response(jsonify(stock[collection]), 200)
        return res
    res = make_response(jsonify({"error": "Not Found"}), 200)
    return res


@app.route("/stock/<collection>/<member>")
def get_member(collection, member):
    if collection in stock:
        if member in stock[collection]:
            res = make_response(jsonify(stock[collection][member]), 200)
            return res
    res = make_response(jsonify({"error": "Not Found"}), 200)
    return res


# @app.route("/stock/<collection>", methods=["PUT"])
# def put_collection(collection):
#     req = request.get_json()
#     if collection in stock:
#         stock[collection] = req
#         res = make_response(jsonify({"msg": "Collection Updated"}), 200)
#         return res
#     stock[collection] = req
#     res = make_response(jsonify({"msg": "Collection Created"}), 201)
#     return res


@app.route("/stock/<collection>", methods=["PUT"])
def put_collection(collection):
    req = request.get_json()
    if collection in stock:
        for key, value in req.items():
            stock[collection][key] = value

        res = make_response(jsonify({"msg": "Collection Updated"}), 200)
        return res
    stock[collection] = req
    res = make_response(jsonify({"msg": "Collection Created"}), 201)
    return res


@app.route("/stock/<collection>", methods=["DELETE"])
def delete_collection(collection):
    if collection in stock:
        del stock[collection]
        res = make_response(jsonify({"msg": "Collection Deleted"}), 204)
        return res

    res = make_response(jsonify({"msg": "Collection is not Present"}), 404)
    return res


@app.route("/stock/<collection>/<member>", methods=["DELETE"])
def delete_member(collection, member):
    if collection in stock:
        if member in stock[collection]:
            del stock[collection][member]
            res = make_response(jsonify({"msg": f"{member} Deleted"}), 204)
            return res

    res = make_response(jsonify({"msg": "Member is not Present"}), 404)
    return res


if __name__ == '__main__':
    app.run(debug=True, port=5001)

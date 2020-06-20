from flask import Flask, jsonify, abort, make_response, request
from models import finances

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}),
                         404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}),
                         400)


@app.route("/api/v1/finances/", methods=["GET"])
def finances_list_api_v1():
    return jsonify(finances.all())


@app.route("/api/v1/finances/<int:finance_id>", methods=["GET"])
def get_finance(finance_id):
    finance = finances.get(finance_id)
    if not finance:
        abort(404)
    return jsonify({"finance": finance})


@app.route("/api/v1/finances/", methods=["POST"])
def create_finance():
    if not request.json or not 'title' in request.json:
        abort(400)
    finance = {
        'id': finances.all()[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'kategoria': request.json['kategoria'],
        'kwota': request.json['kwota'],
        'przychod': request.json.get('przychod', False),
    }
    finances.create(finance)
    return jsonify({'finance': finance}), 201


@app.route("/api/v1/finances/<int:finance_id>", methods=['DELETE'])
def delete_finance(finance_id):
    result = finances.delete(finance_id)
    if not result:
        abort(404)
    return jsonify({'result': result})


@app.route("/api/v1/finances/summary", methods=["GET"])
def present_results():
    finance = finances.count_budget()
    finance = finance["total"]
    if not finance:
        abort(404)
    return jsonify({"finance": finance})


@app.route("/api/v1/finances/summary/category", methods=["GET"])
def present_category_results():
    categories_finance = finances.categories()
    if not categories_finance:
        abort(404)
    return jsonify(categories_finance)


if __name__ == "__main__":
    app.run(debug=True)

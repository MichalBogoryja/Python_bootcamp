from flask import jsonify, abort, request
from models import financesSQL
from app import app, db_file


@app.route("/api/v1/finances/", methods=["GET"])
def finances_list_api_v1():
    return jsonify(financesSQL.all(db_file))


@app.route("/api/v1/finances/<int:finance_id>", methods=["GET"])
def get_finance(finance_id):
    finance = financesSQL.get(finance_id, db_file)
    if not finance:
        abort(404)
    return jsonify({f"finance {finance_id}": finance})


@app.route("/api/v1/finances/", methods=["POST"])
def create_finance():
    if not request.json or 'title' not in request.json:
        abort(400)
    finance = (
        request.json['title'],
        request.json.get('description', ""),
        request.json['kategoria'],
        request.json['kwota'],
        request.json.get('przychod', 0)
    )
    financesSQL.create(finance, db_file)
    return jsonify({'finance': finance}), 201


@app.route("/api/v1/finances/<int:finance_id>", methods=['DELETE'])
def delete_finance(finance_id):
    result = financesSQL.delete(finance_id, db_file)
    if not result:
        abort(404)
    return jsonify({'result': result})


@app.route("/api/v1/finances/<int:finance_id>", methods=['PUT'])
def update_finance(finance_id):
    finance = (
        request.json.get('title'),
        request.json.get('description'),
        request.json.get('kategoria'),
        request.json.get('kwota'),
        request.json.get('przychod')
    )
    result = financesSQL.update(finance_id, db_file, title=finance[0],
                                description=finance[1], kategoria=finance[2],
                                kwota=finance[3], przychod=finance[4])
    if not result:
        abort(404)
    return jsonify({'result': result})


@app.route("/api/v1/finances/summary", methods=["GET"])
def present_results():
    finance = financesSQL.count_budget(db_file)
    finance = finance["total"]
    if not finance:
        abort(404)
    return jsonify({"finance": finance})


@app.route("/api/v1/finances/summary/category", methods=["GET"])
def present_category_results():
    categories_finance = financesSQL.categories(db_file)
    if not categories_finance:
        abort(404)
    return jsonify(categories_finance)

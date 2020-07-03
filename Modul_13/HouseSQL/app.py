from flask import Flask, jsonify, make_response

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"
db_file = "database.db"


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}),
                         404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}),
                         400)


from . import views

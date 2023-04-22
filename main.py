import flask
from flask import Flask, request

app = Flask(__name__)
userId="1"
json = flask.json.jsonify(userId) 
request = flask.json.jsonify(userId)


@app.route('/login', methods=['GET', 'POST'])
def login():
    with app.app_context():
        if request.method == 'GET':
            request = flask.json.jsonify(userId)
            return request


@app.route('/post_json', methods=['POST'])
def process_json():
    with app.app_context():
        content_type = request.headers.get('Content-Type')
        if  content_type == 'application/json':
            json = request.json
            return json
        else:
            return 'Content-Type not supported!'



if __name__ == '__main__':
    app.run(debug=True)
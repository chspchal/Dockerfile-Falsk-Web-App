from flask import Flask, request
# import resquests

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    return "Hello, world!"

@app.route('/mainpage', methods=["GET"])
def mainpage():
    return "This is the main page"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

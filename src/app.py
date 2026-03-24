from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api/hello")
def hello():
    return jsonify({"message": "hello from calculator-api"})


# TODO: /health endpoint is missing — add it here


if __name__ == "__main__":
    app.run(debug=True, port=5000)

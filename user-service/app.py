from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "User Service",
        "status": "running"
    })

@app.route("/users")
def users():
    return jsonify([
        {"id": 1, "name": "Kavin"},
        {"id": 2, "name": "Ajay"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

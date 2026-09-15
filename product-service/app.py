from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "Product Service",
        "status": "running"
    })

@app.route("/products")
def products():
    return jsonify([
        {"id": 1, "name": "Laptop"},
        {"id": 2, "name": "Keyboard"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

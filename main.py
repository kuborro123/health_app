from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "<h1>Welcome to my Render-hosted Flask App!</h1>"

# API route example
@app.route("/api/hello", methods=["GET"])
def hello():
    name = request.args.get("name", "World")
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

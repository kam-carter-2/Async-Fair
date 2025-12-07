from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/hello", methods=["GET"])
def hello():
    name = request.args.get("name", "World")
    return jsonify({"message": f"Hello, {name}!"})

@app.route("/healthz")
def health():
    return "ok", 200

if __name__ == "__main__":
    # Bind to 0.0.0.0 for container environments
    app.run(host="0.0.0.0", port=int(__import__("os").environ.get("PORT", 8080)))

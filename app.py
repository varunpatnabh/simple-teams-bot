from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running 🚀", 200

@app.route("/api/messages", methods=["POST"])
def bot():
    try:
        data = request.json

        return jsonify({
            "type": "message",
            "text": "Hello from bot 👋"
        })

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
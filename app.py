from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/search-alert", methods=["POST"])
def alert():
    return jsonify({
        "response_type": "in_channel",
        "text": "✅ Bot is working! Slack command received."
    })

if __name__ == "__main__":
    app.run(port=3000)


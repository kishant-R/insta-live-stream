from flask import Flask, request

app = Flask(__name__)

# Temporary token (we will update later)
VERIFY_TOKEN = "test_token"

@app.route("/", methods=["GET"])
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge, 200
    return "Verification failed", 403


@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    print("Incoming webhook:", data)
    return "Event Received", 200


if __name__ == "__main__":
    app.run(port=5000)

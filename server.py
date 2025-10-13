from flask import Flask, jsonify, request, Response
from flask_cors import CORS

# Init
app = Flask(__name__)

# Don't worry about this! Just some required security stuff; look into CORS and cross-site-scripting (XSS) if you're interested!
CORS(app)

# API endpoint!
@app.get("/api/your-mom")
def home():
    return Response("Error: file too big!", status=413)

# Place endpoints in this space; they define functions/routes the app will save and look out for when requests come in
# It'll parse and match accordingly; otherwise, it'll reject with a 404 error

if __name__ == "__main__":
    # Change port if necessary
    app.run(host="localhost", port=8080)



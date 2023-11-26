from flask import Flask, request, jsonify 
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def endpoint():
    return "Home"

@app.get("/test")
def test():
    try:
        data = request.args.get('data')
        print("request arguments: ", data)
        if data:
            return "aj data mam", 200
            response = requests.post("", data)
            if response:
                print("AI response: ", response)
                return jsonify({'status': 'success', 'data': response}), 200
            else:
                return jsonify({'status': 'error', 'message': 'Could not fetch response from AI'}), 400
        else:
            return "sicko ok", 200

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


if __name__ == "__main__":
    app.run(port=8080, debug=True)
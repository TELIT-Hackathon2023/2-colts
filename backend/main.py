from flask import Flask, request, jsonify 
import requests

app = Flask(__name__)

@app.route("/")
def endpoint():
    return "Home"

@app.get("/test")
def getTest():
    return "OK"

@app.post("/test")
def test():
    try:
        data = request.get_json()
        print(data)
        if data:
            response = requests.post("api", json={"key": "value"})
            print(response)
            return jsonify({'status': 'success', 'data': data})
        else:
            return jsonify({'status': 'error', 'message': 'No JSON data found in the request body'}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
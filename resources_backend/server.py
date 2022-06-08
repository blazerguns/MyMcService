from flask import Flask, jsonify, make_response, request
import requests

app = Flask(__name__)



@app.route('/resource')
def hello():
    resid_id = request.args.get('rid', None)
    token = request.args.get('token', None)
    try:
        result = requests.get("http://iserv:3000/verify?token={token}".format(token=token)).json()
        if (result['status'] == "denied"):
            return jsonify({"status": "resource denied"}), 200
    except requests.exceptions.RequestException:
        print("Error at resource check")
        return jsonify({"status": "resource denied"}), 200
    
    responseData = {"some": "valuable resource for id {resid_id}".format(resid_id=resid_id)}
    responseData['status'] = 'Ready'
    return jsonify(responseData), 200
    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port='3000')
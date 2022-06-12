import flask
from flask import request, jsonify, Response
import json
from flask_ngrok import run_with_ngrok
from flask_cors import CORS, cross_origin
import pandas as pd
import sqlite3
import constant as constant
import service as service
app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)
run_with_ngrok(app)




@app.route('/data', methods=['POST'])
def add_item():
    # Get item from the POST body
    req_data = request.get_json()
    firstname = req_data['firstname']
    id = req_data['id']
    lastname = req_data['lastname']

    # Add item to the list
    res_data = service.add_to_list(id,firstname,lastname)

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')
    return response

@app.route('/data', methods=['GET'])
def get_all_items():
    # Get items from the helper
    res_data = service.get_all_items()
    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')
    return response

if __name__ == '__main__':
    app.run()
"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/add_member', methods=['POST'])
def add_members():
    new_member = request.json
    member = jackson_family.add_member(new_member)
    if member != None:
        members = jackson_family.get_all_members()
        response = {
            "new_added": member,
            "family": members
        }

        return jsonify(response), 200
    else:
        response = {
        "response": f"member by first name {new_member['first_name']} exist",
        }
        return jsonify(response), 400

@app.route('/delete_member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    member = jackson_family.delete_member(member_id)
    if member == None:
        response = {
        "response": f"member by id {member_id} not exist",
        }
        return jsonify(response), 404
    else:
        response = {
            "done": True
        }
        return jsonify(response), 200

@app.route('/get_member_by_id/<int:member_id>', methods=['GET'])
def get_member_by_id(member_id):

    member = jackson_family.get_member(member_id)
    if len(member) == 0:
        response = {
        "response": f"member by id {member_id} not exist",
        }
        return jsonify(response), 404
    else:
        return jsonify(member[0]), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)

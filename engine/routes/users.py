from flask import Blueprint, request, jsonify
from models.users import User

main = Blueprint('routes', __name__)


@main.route('/register', methods=["POST"])
def register():
  request_data = request.get_json()
  first_name = request_data.get("first_name")
  last_name = request_data.get("last_name")
  email = request_data.get("email")
  empty_field_exists = first_name == None or last_name == None or email == None
  if empty_field_exists: return {"error":"first_name, last_name, and email cannot be empty fields."}
  user = User(**request_data)
  db.session.add(user)
  json_response = jsonify(user.to_json())
  return json_response
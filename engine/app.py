from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import os
from sqlalchemy.sql import func
from flask_migrate import Migrate



class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'<User {self.first_name} {self.last_name}>'
    
    def to_dict(self):
       return dict(id=self.id, first_name=self.first_name, last_name=self.last_name, email=self.email)

@app.route("/register", methods=["POST"])
def register():
  request_data = request.get_json()
  first_name = request_data.get("first_name")
  last_name = request_data.get("last_name")
  email = request_data.get("email")
  empty_field_exists = first_name == None or last_name == None or email == None
  if empty_field_exists: return {"error":"first_name, last_name, and email cannot be empty fields."}
  user = User(**request_data)
  db.session.add(user)
  db.session.commit()
  json_response = jsonify(user.to_dict())
  return json_response

@app.route("/users")
def get_users():
   users = User.query.all()
   json_response = [user.to_dict() for user in users]
   return json_response
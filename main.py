#import dependancies
import os
from datetime import timedelta
from flask import Flask
from flask_migrate import Migrate
from flask_restful import reqparse, Resource
from models import db, User
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from auth import auth_bp, jwt, admin_required
from flask_jwt_extended import jwt_required
from flask import Blueprint

#configure my app
app = Flask(__name__)
CORS(app, origins='http://localhost:5173')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
#postgresql://deriv_app_97ig_user:WxL0neAJVKSBM3G8MO57vNWpkC8OQydw@dpg-cnvka1ect0pc73dnentg-a.oregon-postgres.render.com/deriv_app_97ig
app.config['SECRET_KEY'] = 'navigator_deriv'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours = 1)
#blueprints
app.register_blueprint(auth_bp)
db.init_app(app)
jwt.init_app(app)
migrate = Migrate(app, db)

@app.route('/home')
def home():
    return "home to you and me"

if __name__ == '__main__':
    app.run(debug=True)
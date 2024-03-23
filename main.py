#import dependancies
import os
from datetime import timedelta
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import reqparse, Resource
from models import db, User
from auth import auth_bp, jwt, admin_required
from flask_jwt_extended import jwt_required
from flask import Blueprint

#configure my app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
#postgresql://deriv_navigator_user:COZNJTkY2FlOGiMb7Th6mLtxgD4fcClZ@dpg-cnuo5s8l6cac73ak0vfg-a.oregon-postgres.render.com/deriv_navigator
#postgresql://deriv_navigator_user:COZNJTkY2FlOGiMb7Th6mLtxgD4fcClZ@dpg-cnuo5s8l6cac73ak0vfg-a/deriv_navigator
app.config['SECRET_KEY'] = 'navigator_deriv'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours = 1)
#blueprints
app.register_blueprint(auth_bp)
CORS(app)
db.init_app(app)
jwt.init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)
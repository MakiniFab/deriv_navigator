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
CORS(app) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
#postgresql://master_navi_csa0_user:P6W9H8g7zy0wqthMEFkGmjGZo0cKcug2@dpg-cnub59sf7o1s73avvv1g-a.oregon-postgres.render.com/master_navi_csa0
app.config['SECRET_KEY'] = 'navigator_deriv'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours = 1)
#blueprints
app.register_blueprint(auth_bp)
db.init_app(app)
jwt.init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)
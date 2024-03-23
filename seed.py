# Import necessary modules and classes
from models import db, User
from werkzeug.security import generate_password_hash
from main import app

def create_admin_user():
    with app.app_context():
        admin_user_data = {
            'first_name': 'Navigator',
            'account': 'navigator',
            'email': 'navigator@gmail.com',
            'phone_no': +254704579253,
            'admin': True,
            'password': 'navigator'
        }

        # Generate password hash
        password_hash = generate_password_hash(admin_user_data['password'])

        # Modify user data to include hashed password
        admin_user_data['password'] = password_hash

        # Create admin user
        admin_user = User(**admin_user_data)
        db.session.add(admin_user)
        db.session.commit()

if __name__ == '__main__':


    # Create admin user
    create_admin_user()
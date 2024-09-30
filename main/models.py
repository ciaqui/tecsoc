from datetime import datetime
from . import db, login_manager
from flask_login import UserMixin
import secrets


#############################
#                           #
#       User Stuff          #
#                           #
#############################

class User(UserMixin, db.Model):
    # Datebase Columns 
    id = db.Column(db.String(20), primary_key=True, default=secrets.token_hex(10)) # Must be randomly generated
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    date_joined = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    # Links (ForeignKeys)
    # Add here

    # Relationships
    # Add here


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
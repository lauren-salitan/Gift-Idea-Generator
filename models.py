from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from flask_bcrypt import Bcrypt

# bcrypt = Bcrypt(app)
bcrypt = Bcrypt()  

def init_bcrypt(app):
    bcrypt.init_app(app)

# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True, unique=True)
#     email = db.Column(db.String(120), index=True, unique=True)
#     password_hash = db.Column(db.String(128))
#     recipient_profiles = db.relationship('RecipientProfile', backref='author', lazy='dynamic')

#     def set_password(self, password):
#         self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)
    
#     def is_active(self):
#         """True, as all users are active."""
#         return True

#     def get_id(self):
#         """Return the email address to satisfy Flask-Login's requirements."""
#         return self.id

#     @classmethod
#     def authenticate(cls, username, password):
#         user = cls.query.filter_by(username=username).first()
#         if user and bcrypt.check_password_hash(user.password_hash, password):
#             return user
#         return None

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    recipient_profiles = db.relationship('RecipientProfile', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
    
    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.id


class RecipientProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(100))
    birthday = db.Column(db.DateTime)
    gender = db.Column(db.String(10))
    relationship = db.Column(db.String(100))
    interests = db.Column(db.Text)
    occasion = db.Column(db.String(100))
    budget = db.Column(db.Float)
    additional_details = db.Column(db.Text)
    created_at = db.Column(db.DateTime, index=True, default=datetime.now)

class GiftIdea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipient_profile_id = db.Column(db.Integer, db.ForeignKey('recipient_profile.id'))
    suggestion_text = db.Column(db.Text)
    external_link = db.Column(db.String(250))
    created_at = db.Column(db.DateTime, index=True, default=datetime.now)

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)
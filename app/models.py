from app import db
from uuid import uuid4

class User(db.Model):
	id = db.Column(db.String(36), primary_key=True, default=str(uuid4()))
	firstName = db.Column(db.String(100), nullable=False)
	lastName = db.Column(db.String(100), nullable=False)
	email = db.Column(db.String(100), nullable=False)
	password = db.Column(db.String(100), nullable=False)


class AsciiImg(db.Model):
	id = db.Column(db.String(36), primary_key=True, default=str(uuid4()))
	img = db.Column(db.String(2000), nullable=False)
	ascci = db.Column(db.String(2000), nullable=False)
	resolution = db.Column(db.Integer, nullable=False)
	colour = db.Column(db.Boolean, nullable=False)
	highlights = db.Column(db.Integer, nullable=False)
from app import db
from datetime import datetime


class Post(db.Model):
	pk = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(255), nullable=False, unique=True)
	body = db.Column(db.Text)
	author = db.Column(db.String(100), default='Jesco')
	created = db.Column(db.DateTime, default=datetime.utcnow)
	
	def __repr__(self):
		return f'{self.title}'

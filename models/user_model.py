from flask_sqlalchemy import SQLAlchemy

bd = SQLAlchemy()

class User(bd.Model):
    __tablename__ = 'users'
    id = bd.Column(bd.Integer, primary_key=True)
    name = bd.Column(bd.String(100), nullable=False)
    email = bd.Column(bd.String(100), nullable=False)
    password = bd.Column(bd.Integer, nullable=False)

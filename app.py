import os
from flask import Flask
from config import Config
from controllers.user_controller import UserController
from models.user_model import User, bd

app = Flask(__name__, template_folder=os.path.join('view', 'templates'))
app.config.from_object(Config)

bd.init_app(app)

with app.app_context():
    bd.create_all()

app.add_url_rule('/index.html', 'index', UserController.index)
app.add_url_rule('/register.html', 'register', UserController.register, methods=['POST', 'GET'])


if __name__ == "__main__":
    app.run(debug=True, port=5002)

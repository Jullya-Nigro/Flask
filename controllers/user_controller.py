from models.user_model import User, bd
from flask import render_template, request, redirect, url_for

class UserController:
    @staticmethod
    def index():
        users = User.query.all()
        return render_template('index.html', users=users)
    
    @staticmethod
    def register():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']

            new_user = User(name=name, email=email, password=password)
            bd.session.add(new_user)
            bd.session.commit()

            return redirect(url_for('index'))
        
        return render_template('register.html')
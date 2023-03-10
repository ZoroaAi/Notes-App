from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods= ['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category="success")
                login_user(user, remember= True)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect password, Try Again", category="Error")
        else:
            flash("Email does not exist", category="Error")
            
    return render_template('login.html', user = current_user)


@auth.route('/sign-up', methods= ['GET','POST'])
def sign_up():
    #  Form Validation
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists', category="Error")
        elif len(email) < 7:
            flash('Email must be longer than 6 characters', category='Error')
        elif len(firstName)<2:
            flash('First Name must be longer than 1 characters', category='Error')
        elif password1 != password2:
            flash('Password does not match', category='Error')
        elif len(password1) < 7:
            flash('Password must be longer than 6 characters', category='Error')
        else:
            # Add user to Database
            new_user = User(email= email, firstName=firstName, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember= True)
            flash('Account Created', category = 'Success')
            return redirect(url_for('views.home'))
        
    return render_template('sign_up.html', user = current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods= ['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html')


@auth.route('/sign-up', methods= ['GET','POST'])
def sign_up():
    #  Form Validation
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 7:
            flash('Email must be longer than 6 characters', category='Error')
        elif len(firstName)<2:
            flash('First Name must be longer than 1 characters', category='Error')
        elif password1 != password2:
            flash('Password does not match', category='Error')
        elif len(password1) < 7:
            flash('Password must be longer than 6 characters', category='Error')
        else:
            # Add user to Database
            flash('Account Created', category = 'Success')
            pass
        
    return render_template('sign_up.html')

@auth.route('/logout')
def logout():
    return '<p>Logout</p>'
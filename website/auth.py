from flask import Blueprint, render_template, request as req, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    data = req.form
    print(data)
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return '<p>Logout</p>'

@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
    if req.method == 'POST':
        email = req.form.get('email')
        firstName = req.form.get('firstName')
        password1 = req.form.get('password1')
        password2 = req.form.get('password2')

        if len(email) > 4:
            flash('email must be greater than 4 characters', category='error')
        elif len(firstName) < 2:
            flash('first name must be greater than 1 character', category='error')
        elif password1 != password2:
            flash('passwords dont\'t match', category='error')
        elif len(password1) < 7:
            flash('password must be at least 7 characters', category='error')
        else:
            flash('Account created!', category='success')
            
    return render_template('sign_up.html')
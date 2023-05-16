from ConstruAccion import app,db
from flask import render_template, redirect, request, url_for, flash,abort
from flask_login import login_user,login_required,logout_user
from ConstruAccion.models import User, Obra
from ConstruAccion.forms import LoginForm, RegistrationForm, AltaObra
from werkzeug.security import generate_password_hash, check_password_hash

#init.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


# Create a login manager object
login_manager = LoginManager()

app = Flask(__name__)

# Often people will also separate these into a separate config.py file
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

# We can now pass in our app to the login manager
login_manager.init_app(app)

# Tell users what view to go to when they need to login.
login_manager.login_view = "login"

@app.route('/')
def home():
    return render_template('ConstruAccion/templates/home.html')


@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')

@app.route('/mkt')
@login_required
def mkt():
    return render_template('mkt.html')

@app.route('/obra')
@login_required
def obra():
    return render_template('obra.html')

@app.route('/admon')
@login_required
def admon():
    return render_template('admon.html')

@app.route('/alta_obra', methods=['GET', 'POST'])
@login_required
def alta_obra():
    form=AltaObra()

    if form.validate_on_submit():
        obra = Obra(nombre_obra=form.nombre_obra.data,
                    calle_obra=form.calle_obra.data,
                    numero_obra=form.numero_obra.data,
                    colonia_obra=form.colonia_obra.data,
                    municipio_obra=form.municipio_obra.data,
                    estado_obra=form.estado_obra.data,
                    cp_obra=form.cp_obra.data)

        db.session.add(obra)
        db.session.commit()
        return redirect(url_for('obra'))
    return render_template('alta_obra.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You logged out!')
    return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        # Grab the user from our User Models table
        user = User.query.filter_by(email=form.email.data).first()

        # Check that the user was supplied and the password is right
        # The verify_password method comes from the User object
        # https://stackoverflow.com/questions/2209755/python-operation-vs-is-not

        if user.check_password(form.password.data) and user is not None:
            #Log in the user

            login_user(user)
            flash('Logged in successfully.')

            # If a user was trying to visit a page that requires a login
            # flask saves that URL as 'next'.
            next = request.args.get('next')

            # So let's now check if that next exists, otherwise we'll go to
            # the welcome page.
            if next == None or not next[0]=='/':
                next = url_for('welcome_user')

            return redirect(next)
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering! Now you can login!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering! Now you can login!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

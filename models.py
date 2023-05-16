from ConstruAccion import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
# By inheriting the UserMixin we get access to a lot of built-in attributes
# which we will be able to call in our views!
# is_authenticated()
# is_active()
# is_anonymous()
# get_id()


# The user_loader decorator allows flask-login to load the current user
# and grab their id.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):

    # Create a table in the db
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        # https://stackoverflow.com/questions/23432478/flask-generate-password-hash-not-constant-output
        return check_password_hash(self.password_hash,password)

class Obra(db.Model, UserMixin):

    # Create a table in the db
    __tablename__ = 'obras'

    id = db.Column(db.Integer, primary_key = True)
    nombre_obra = db.Column(db.String(64), unique=True, index=True)
    calle_obra = db.Column(db.String(64), unique=False, index=True)
    numero_obra = db.Column(db.Integer, unique=False, index=True)
    colonia_obra = db.Column(db.String(64), unique=False, index=True)
    municipio_obra = db.Column(db.String(64), unique=False, index=True)
    estado_obra = db.Column(db.String(64), unique=False, index=True)
    cp_obra = db.Column(db.Integer, unique=False, index=True)

    def __init__(self, nombre_obra, calle_obra, numero_obra, colonia_obra, municipio_obra, estado_obra, cp_obra):
        self.nombre_obra = nombre_obra
        self.calle_obra = calle_obra
        self.numero_obra = numero_obra
        self.colonia_obra = colonia_obra
        self.municipio_obra = municipio_obra
        self.estado_obra = estado_obra
        self.cp_obra = cp_obra

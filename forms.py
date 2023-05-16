from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords Must Match!')])
    pass_confirm = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register!')

class AltaObra(FlaskForm):
    nombre_obra = StringField('Nombre de Obra', validators=[DataRequired()])
    calle_obra = StringField('Calle', validators=[DataRequired()])
    numero_obra = StringField('Numero exterior', validators=[DataRequired()])
    colonia_obra = StringField('Colonia', validators=[DataRequired()])
    municipio_obra = StringField('Municipio', validators=[DataRequired()])
    estado_obra = StringField('Estado', validators=[DataRequired()])
    cp_obra = StringField('Codigo Postal', validators=[DataRequired()])
    submit = SubmitField('Alta')

def validate_email(self, email):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError('Email has been registered')
def validate_username(self, username):
        if User.query.filter_by(username=self.username.data).first():
            raise ValidationError('Username has been registered')

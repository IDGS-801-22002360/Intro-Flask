from wtforms import Form, StringField, PasswordField, BooleanField, SubmitField, validators, IntegerField, RadioField

class userForm(Form):
    matricula = IntegerField('Matricula', [
        validators.DataRequired(message='Este campo es requerido'),
        ])
    nombre = StringField('Nombre', [
        validators.DataRequired(message='Este campo es requerido'),
        validators.Length(min=3, max=25)
        ])
    apellido = StringField('Apellido', [
        validators.DataRequired(message='Este campo es requerido'),
        validators.Length(min=3, max=25)
        ])
    email = StringField('Email', [
        validators.DataRequired(message='Este campo es requerido'),
        validators.Length(min=6, max=35)
        ])


class zodiacoForm(Form):
    Nombre = StringField('Nombre', [
        validators.DataRequired(message='Este campo es requerido'),
        ])
    ApellidoPaterno = StringField('Apellido Paterno', [
        validators.DataRequired(message='Este campo es requerido'),
        ])
    ApellidoMaterno = StringField('Apellido Materno', [
        validators.DataRequired(message='Este campo es requerido'),
        ])
    DiaNacimiento = IntegerField('Día de Nacimiento', [
        validators.DataRequired(message='Este campo es requerido'),
        ])
    MesNacimiento = IntegerField('Mes de Nacimiento', [
        validators.DataRequired(message='Este campo es requerido'),
        ])
    AnioNacimiento = IntegerField('Año de Nacimiento', [
        validators.DataRequired(message='Este campo es requerido'),
        ])
    Sexo = RadioField('Sexo', choices=[('H', 'Hombre'), ('M', 'Mujer')], validators=[validators.DataRequired(message='Este campo es requerido')])
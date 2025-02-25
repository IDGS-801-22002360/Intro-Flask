from wtforms import Form, StringField, PasswordField, BooleanField, SubmitField, validators, IntegerField

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
    
    

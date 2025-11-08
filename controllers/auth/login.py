
from flask import Blueprint, render_template, request, redirect, url_for,session, flash
from models.auth.registro import Registro 
from utils.db import db
login = Blueprint('login',__name__,template_folder='templates')




@login.route('/')
def index():
    return redirect(url_for('login.login_in'))

@login.route('/login', methods = ['GET','POST'])
def login_in():
    if request.method == 'POST' and 'correo' in request.form:
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        user = Registro.query.filter_by(correo=correo).first()
        if user and user.check_password(user.contrasena, contrasena):
            session['user'] = user.usuario
            #session.pop('user', None)
            session.permanent = True
            return redirect(url_for('dashboard.index'))
        else :
            if not correo:
                error = "Debes ingresar un correo"
            elif not contrasena:
                error = "Debes ingresar una contraseña"
            else:
                error="El usuario o contraseña son incorrectos."
            return render_template('/auth/login.html', error = error) 
    else:
        return render_template('/auth/login.html')

@login.route('/registro', methods = ['GET','POST'])
def registro_page():
    error = None
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        validUser = Registro.query.filter_by(usuario = usuario).first()
        validEmail = Registro.query.filter_by(correo = correo).first()
    
        if not usuario:
            error = "Debes ingresar un usuario"
        elif not correo:
            error = "Debes ingresar un correo"
        elif not contrasena:
            error = "Debes ingresar una contraseña"
        elif validUser != None:
            error = "El usuario ya existe, debes ingresar otro diferente"
        elif validEmail != None:
            error = "El correo ya existe, debes ingresar otro diferente"
        else:
            registro = Registro(usuario,correo,contrasena)
            db.session.add(registro)
            db.session.commit()
            mns = "El usuario se registro correctamente, inicie sesión para poder ingresar"
            flash(mns)
            return redirect(url_for('login.login_in'))
    return render_template('/auth/registro.html', error = error)

@login.route('/logout')
def logout():
    session.pop('user', None)
    session.clear()
    return redirect(url_for('login.login_in'))
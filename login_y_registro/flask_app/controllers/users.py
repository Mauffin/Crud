#rutas 
from atexit import register
from flask import render_template, redirect ,session,request,flash
from flask_app import app
from flask_app.models.users import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['post'])
def register():
    if not User.valida_usuario(request.form):
        return redirect('/')
    
    pwd = bcrypt.generate_password_hash(request.form['password'])

    formulario={
        'first_name':request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pwd
    }

    id = User.save(formulario)
    
    session['user_id'] = id

    return redirect('/dashboard')

@app.route('/login', methods=['post'])
def login():
    user = User.get_by_email(request.form)
    
    if not user:
        flash("email no encontrado", 'login')
        return redirect('/')

    if not bcrypt.check_password_hash(user.password,request.form['password']):
        flash("password incorrecto",'login')
        return redirect('/')

    session['users_id'] = user.id
    return redirect('/dashboard')

@app.route("/dashboard")
def dashboard():
    if 'user_id' not in session:
        return redirect('/')

    data = {
        "id": session['user_id']
    }

    user = User.get_by_id(data)

    return render_template('dashboard.html',user=user)


@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')

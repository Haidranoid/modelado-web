from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'secreto_super_seguro_123'  # Cambia esto por algo fuerte en producción

# Simulamos una base de datos
usuarios = {
    'admin': '1234',
    'user': 'test'
}


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['username']
        clave = request.form['password']

        if usuario in usuarios and usuarios[usuario] == clave:
            session['usuario'] = usuario
            return redirect(url_for('home'))
        else:
            flash('Usuario o contraseña incorrectos.')
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/home')
def home():
    if 'usuario' in session:
        return render_template('home.html', usuario=session['usuario'])
    else:
        flash('Debes iniciar sesión primero.')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('usuario', None)
    flash('Sesión cerrada exitosamente.')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)

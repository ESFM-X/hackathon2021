### Flask 
from flask_wtf.csrf import  CSRFError

### Local
from resources import registro as r
from resources import (
    index, convocatoria, aviso_privacidad,
    registro, registrar, contacto,
    verificar, handle_csrf_error, desuscribir
)
from core import app

app.route('/')(index)

app.route('/convocatoria')(convocatoria)

app.route('/avisodeprivacidad')(aviso_privacidad)

app.route('/registro', methods = ['GET'])(registro)

app.route('/registro', methods = ['POST'])(registrar)

app.route('/contacto')(contacto)  

app.route('/verify/<email>')(verificar)

#app.route('/desuscribir/<email>')(desuscribir)

app.errorhandler(CSRFError)(handle_csrf_error)
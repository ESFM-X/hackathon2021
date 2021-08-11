import requests
from config.settings import api_url
from flask import jsonify
def check(datos):
    correos = organize_data(datos)
    response = requests.get(api_url, {'correos':correos} )
    if response.status_code != 200:
        return {
            'status':False, 
            'error_message':'Hubo un error con nuestros servidores, inténtalo de nuevo en unos minutos.',
        }
    correos_repetidos = response.json()['datos']
    if correos_repetidos:
        return {
            'status':False, 
            'error_message':'Los los siguientes correos ya han sido registrados: ' + ' '.join(correos_repetidos),
        }
    return {
            'status':True, 
            'datos': datos
        }
def organize_data(datos):
    """
    Regresa los correos de los integrantes en un string separados por un "*"
    """
    correos = []
    
    for i in range(int(datos['cantidad'])):
        correos.append(datos[f'correo_{i}'])
    
    return  '*'.join(correos)

def registar(datos):
    response = requests.post(api_url,  datos)
    if response.status_code != 201:
        return {
            'status':False, 
            'error_message':'Hubo un error con nuestros servidores, inténtalo de nuevo en unos minutos.',
        }
    return {
            'status':True, 
            'id': response.json()['token'],
        }

def verificar(email_encrypted):
    response = requests.put(api_url,  {'email_encrypted':email_encrypted })
    if str(response.status_code)[0] == '4':
        return {
            'status':False, 
            'error_message':response.json()['error'],
        }
    elif response.status_code != 200:
        return {
            'status':False, 
            'error_message':'Hubo un error con nuestros servidores, inténtalo de nuevo en unos minutos.',
        }
    return  {
            'status':True, 
        }
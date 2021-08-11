import requests
from colorama import Fore, Style
BASE = 'http://127.0.0.1:5000/'

datos = [
    {'ruta':'/registro', 
     'args':{
            'list': 'Juan', 
            },
    'metodo':requests.post
    },
]

for dato in datos:
    print("#"*30, f'Ruta: {dato["ruta"]} Método: {dato["metodo"]}')

    print('Credenciales y datos correctos:', end = ' ')
    try: 
        response = dato['metodo'](BASE + f'{dato["ruta"]}', dato['args'] )
    except Exception  as e:
        print(f'Error en {dato["ruta"]}\n {e}\n\n\n')
    else:
        if str(response.status_code)[0] == '2':
            print(Fore.GREEN +'[OK]', Style.RESET_ALL)
        else:
            print(Fore.RED +'[NOT]', Style.RESET_ALL,  response.status_code, response.text)

    print('Falta de datos: ', end = ' ')
    response = dato['metodo'](BASE + f'{dato["ruta"]}' )
    if response.status_code == 400:
        print(Fore.GREEN +'[OK]', Style.RESET_ALL)
    else:
        print(Fore.RED +'[NOT]', Style.RESET_ALL, response.status_code, response.text)
    
    print('Método incorrecto: ', end = ' ')
    response =  requests.get(BASE + f'{dato["ruta"]}')
    if str(response.status_code)[0]  == '4':
        print(Fore.GREEN +'[OK]', Style.RESET_ALL)
    else:
        print(Fore.RED +'[NOT]', Style.RESET_ALL, response.status_code, response.text)

    print('Llave incorrecta: ', end = ' ')
    response =  requests.post(BASE + f'{dato["ruta"]}das')
    if response.status_code == 401:
        print(Fore.GREEN +'[OK]', Style.RESET_ALL)
    else:
        print(Fore.RED +'[NOT]', Style.RESET_ALL, response.status_code, response.text)
    print(Style.RESET_ALL)
    print("\n\n\n")
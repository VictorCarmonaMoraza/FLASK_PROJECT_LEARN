from flask import Flask, request

app = Flask(__name__)


#http://localhost:5000/
@app.route("/")
def inicio():
    #app.logger.debug('Nivel debug')
    app.logger.info(f'Entramos al path {request.path}')
    #app.logger.warn('Nivel warning')
    #app.logger.error('Nivel error')
    return "<p>Hola Mundo desde Flask Victor.!</p>"

##http://localhost:5000/saludar/Victor
##En variable de tipo string no hace falta declarar el tipo
@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'Saludos {nombre.upper()}'

##http://localhost:5000/edad/12
##En este caso el tipo que recibe es un parametro de tipo entero
@app.route('/edad/<int:edad>')
def mostrar_edad(edad):
    return f'Tu edad es: {edad +12}'

##http://localhost:5000/edad/12
##En este caso el tipo que recibe es un parametro de tipo entero
@app.route('/edadString2/<edad>')
def mostrar_edad2(edad):
    return f'Tu edad es: {edad +str(12)}'
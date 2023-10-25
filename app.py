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
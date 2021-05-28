from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
# configuracion de base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# generar base de datos
db = SQLAlchemy(app)

# ruta inicial
@app.route('/')
def index():
    return jsonify({ "info": "servidor Flask" })

# importar modelos
from controllers.cUsuario import UsuarioController
from controllers.cCategoria import CategoriaController
from controllers.cNoticia import NoticiaController

# buscar usuario
@app.route('/api/usuarios/login', methods = ["POST"])
def getUsuario():
    # recoger información
    username = request.form.get("username")
    password = request.form.get("password")
    # verificar campos vacios
    if (username and password):
        # buscar información
        data = UsuarioController.getLogin(username=username, password=password)
        return jsonify({ "data": data, "mensaje": "Buscado", "error": False })
    else:
        return jsonify({ "data": [], "mensaje": "Campos vacios", "error": True })

# guardar usuario
@app.route('/api/usuarios/guardar', methods = ["POST"])
def setUsuario():
    # recoger información
    nombre = request.form.get("nombre")
    direccion = request.form.get("direccion")
    telefono = request.form.get("telefono")
    username = request.form.get("username")
    password = request.form.get("password")
    email = request.form.get("email")
    # verificar campos vacios
    if (nombre and direccion and telefono and username and password and email):
        # guardar información
        data = UsuarioController.setUsuario(nombre=nombre, direccion=direccion, telefono=telefono, username=username, password=password, email=email)
        return jsonify({ "data": data, "mensaje": "Guardado", "error": False })
    else:
        return jsonify({ "data": [], "mensaje": "Campos vacios", "error": True })

# buscar categorias
@app.route('/api/categorias', methods = ["POST"])
def getCategorias():
    # buscar información
    data = CategoriaController.getCategorias()
    return jsonify({ "data": data, "mensaje": "Buscado", "error": False })

# buscar noticias
@app.route('/api/noticias', methods = ["POST"])
def getNoticias():
    # buscar información
    data = NoticiaController.getNoticias()
    return jsonify({ "data": data, "mensaje": "Buscado", "error": False })

# buscar noticias visibles
@app.route('/api/noticias/visibles', methods = ["POST"])
def getNoticiasVisibles():
    # buscar información
    data = NoticiaController.getNoticiasVisibles()
    return jsonify({ "data": data, "mensaje": "Buscado", "error": False })

# guardar noticia
@app.route('/api/noticias/guardar', methods = ["POST"])
def setNoticia():
    # recoger información
    nombreNoticia = request.form.get("nombreNoticia")
    descripcion = request.form.get("descripcion")
    nombrePeriodista = request.form.get("nombrePeriodista")
    visible = request.form.get("visible")
    idCategoria = request.form.get("idCategoria")
    horaNoticia = request.form.get("horaNoticia")
    imgNoticia = request.form.get("imgNoticia")
    resumen = request.form.get("resumen")
    # verificar campos vacios
    if (nombreNoticia and descripcion and nombrePeriodista and visible and idCategoria and horaNoticia and imgNoticia and resumen):
        # guardar información
        data = NoticiaController.setNoticia(nombreNoticia=nombreNoticia, descripcion=descripcion, nombrePeriodista=nombrePeriodista, visible=visible, idCategoria=idCategoria, horaNoticia=horaNoticia, imgNoticia=imgNoticia, resumen=resumen)
        if (data):
            return jsonify({ "data": NoticiaController.getNoticias(), "mensaje": "Guardado", "error": False })
        else:
            return jsonify({ "data": [], "mensaje": "Error en BD", "error": True })
    else:
        return jsonify({ "data": [], "mensaje": "Campos vacios", "error": True })

# actualizar noticia
@app.route('/api/noticias/editar', methods = ["POST"])
def setNoticiaUpdate():
    # recoger información
    id = request.form.get("id")
    nombreNoticia = request.form.get("nombreNoticia")
    descripcion = request.form.get("descripcion")
    nombrePeriodista = request.form.get("nombrePeriodista")
    visible = request.form.get("visible")
    idCategoria = request.form.get("idCategoria")
    horaNoticia = request.form.get("horaNoticia")
    imgNoticia = request.form.get("imgNoticia")
    resumen = request.form.get("resumen")
    # verificar campos vacios
    if (id and nombreNoticia and descripcion and nombrePeriodista and visible and idCategoria and horaNoticia and imgNoticia and resumen):
        # editar información
        data = NoticiaController.setNoticiaUpdate(id=id, nombreNoticia=nombreNoticia, descripcion=descripcion, nombrePeriodista=nombrePeriodista, visible=visible, idCategoria=idCategoria, horaNoticia=horaNoticia, imgNoticia=imgNoticia, resumen=resumen)
        if (data):
            return jsonify({ "data": NoticiaController.getNoticias(), "mensaje": "Editado", "error": False })
        else:
            return jsonify({ "data": [], "mensaje": "No existe", "error": True })
    else:
        return jsonify({ "data": [], "mensaje": "Campos vacios", "error": True })

# eliminar noticia
@app.route('/api/noticias/eliminar', methods = ["POST"])
def setNoticiaDelete():
    # recoger información
    id = request.form.get("id")
    # verificar campos vacios
    if (id):
        # eliminar información
        data = NoticiaController.setNoticiaDelete(id=id)
        if (data):
            return jsonify({ "data": NoticiaController.getNoticias(), "mensaje": "Eliminado", "error": False })
        else:
            return jsonify({ "data": [], "mensaje": "No existe", "error": True })
    else:
        return jsonify({ "data": [], "mensaje": "Campos vacios", "error": True })

if __name__=='__main__':
   app.run(debug=True)
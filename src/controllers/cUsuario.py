from app import db
from models.mUsuario import Usuario

class UsuarioController():

    # buscar usuario
    def getLogin(username, password):
        resp = []
        # buscar por usuario y contraseña
        usuarios = Usuario.query.filter_by(username=username, password=password)
        # organizar información
        for usuario in usuarios:
            resp.append({
                "id": usuario.id,
                "nombre": usuario.nombre,
                "direccion": usuario.direccion,
                "telefono": usuario.telefono,
                "username": usuario.username,
                "password": usuario.password,
                "email": usuario.email,
            })
        # devolver lista
        return resp

    # crear usuario
    def setUsuario(nombre, direccion, telefono, username, password, email):
        # crear modelo de usuario
        usuario = Usuario(nombre=nombre, direccion=direccion, telefono=telefono, username=username, password=password, email=email)
        # agregar usuario
        db.session.add(usuario)
        # guardar cambios
        db.session.commit()
        # devolver id
        return { "id": usuario.id }
        
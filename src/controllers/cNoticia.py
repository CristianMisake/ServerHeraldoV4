from app import db
from models.mNoticia import Noticia

class NoticiaController():

    # buscar noticias
    def getNoticias():
        resp = []
        # buscar todas las noticias
        noticias = Noticia.query.all()
        # organizar información
        for noticia in noticias:
            resp.append({
                "id": noticia.id,
                "nombreNoticia": noticia.nombreNoticia,
                "descripcion": noticia.descripcion,
                "nombrePeriodista": noticia.nombrePeriodista,
                "visible": noticia.visible,
                "fechaCreacion": noticia.fechaCreacion,
                "idCategoria": noticia.idCategoria,
                "horaNoticia": noticia.horaNoticia,
                "imgNoticia": noticia.imgNoticia,
                "resumen": noticia.resumen,
            })
        # devolver lista
        return resp

    # buscar visibles
    def getNoticiasVisibles():
        resp = []
        # buscar noticias visibles
        noticias = Noticia.query.filter_by(visible=1)
        # organizar información
        for noticia in noticias:
            resp.append({
                "id": noticia.id,
                "nombreNoticia": noticia.nombreNoticia,
                "descripcion": noticia.descripcion,
                "nombrePeriodista": noticia.nombrePeriodista,
                "visible": noticia.visible,
                "fechaCreacion": noticia.fechaCreacion,
                "idCategoria": noticia.idCategoria,
                "horaNoticia": noticia.horaNoticia,
                "imgNoticia": noticia.imgNoticia,
                "resumen": noticia.resumen,
            })
        # devolver lista
        return resp
    
    # crear noticia
    def setNoticia(nombreNoticia, descripcion, nombrePeriodista, visible, idCategoria, horaNoticia, imgNoticia, resumen):
        # crear modelo de noticia
        noticia = Noticia(nombreNoticia=nombreNoticia, descripcion=descripcion, nombrePeriodista=nombrePeriodista, visible=visible, idCategoria=idCategoria, horaNoticia=horaNoticia, imgNoticia=imgNoticia, resumen=resumen)
        # agregar noticia
        db.session.add(noticia)
        # guardar cambios
        db.session.commit()
        # devolver id
        return { "id": noticia.id }
    
    # actualizar noticia
    def setNoticiaUpdate(id, nombreNoticia, descripcion, nombrePeriodista, visible, idCategoria, horaNoticia, imgNoticia, resumen):
        # buscar noticia
        noticia = Noticia.query.get(id)
        if (noticia):
            # actualizar noticia
            noticia.nombreNoticia = nombreNoticia
            noticia.descripcion = descripcion
            noticia.nombrePeriodista = nombrePeriodista
            noticia.visible = visible
            noticia.idCategoria = idCategoria
            noticia.horaNoticia = horaNoticia
            noticia.imgNoticia = imgNoticia
            noticia.resumen = resumen
            # guardar cambios
            db.session.commit()
            # devolver id
            return { "id": id }
        else:
            return {}
    
    # eliminar noticia
    def setNoticiaDelete(id):
        # buscar noticia
        noticia = Noticia.query.get(id)
        if (noticia):
            # eliminar noticia
            db.session.delete(noticia)
            # guardar cambios
            db.session.commit()
            # devolver id
            return { "id": id }
        else:
            return {}

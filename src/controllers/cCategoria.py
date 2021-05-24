from models.mCategoria import Categoria

class CategoriaController():

    # buscar categorias
    def getCategorias():
        resp = []
        # buscar todas las categorias
        categorias = Categoria.query.all()
        # organizar información
        for categoria in categorias:
            resp.append({
                "id": categoria.id,
                "nombreCategoria": categoria.nombreCategoria,
            })
        # devolver lista
        return resp
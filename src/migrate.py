from app import db
from models.mCategoria import Categoria
# crear base de datos
db.create_all()
# categorias
categoria = Categoria(nombreCategoria="deportes")
categoria2 = Categoria(nombreCategoria="judicial")
categoria3 = Categoria(nombreCategoria="economía")
categoria4 = Categoria(nombreCategoria="sociales")
categoria5 = Categoria(nombreCategoria="entretenimiento")
categoria6 = Categoria(nombreCategoria="salud")
categoria7 = Categoria(nombreCategoria="política")
# datos por default
db.session.add(categoria)
db.session.add(categoria2)
db.session.add(categoria3)
db.session.add(categoria4)
db.session.add(categoria5)
db.session.add(categoria6)
db.session.add(categoria7)
# guardar cambios
db.session.commit()
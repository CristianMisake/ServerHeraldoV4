from app import db

class Categoria(db.Model):
    __tablename__ = 'categorias'

    id = db.Column(db.Integer, primary_key=True)
    nombreCategoria = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return "<Noticia %r>" % self.nombreCategoria
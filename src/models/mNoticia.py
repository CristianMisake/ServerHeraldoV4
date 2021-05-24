from app import db
from datetime import datetime

class Noticia(db.Model):
    __tablename__ = 'noticias'

    id = db.Column(db.Integer, primary_key=True)
    nombreNoticia = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(100), nullable=False)
    nombrePeriodista = db.Column(db.String(100), nullable=False)
    visible = db.Column(db.Integer, nullable=False)
    fechaCreacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    idCategoria = db.Column(db.Integer, nullable=False)
    horaNoticia = db.Column(db.String(10), nullable=False)
    imgNoticia = db.Column(db.String(200), nullable=False)
    resumen = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return "<Noticia %r>" % self.nombreNoticia
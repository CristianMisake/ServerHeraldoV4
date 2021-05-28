# ServerHeraldoV4

## Tener en cuenta:

### Tener instalado:
	python3
	python3-venv

### Crear entorno:
    python3 -m venv venv

### Acceder al entorno:
    source venv/bin/activate

### instalar: flask y sqlalchemy
    pip3 install flask flask-sqlalchemy sqlalchemy

### configuración de flask
    export FLASK_APP=src/app.py

### correr migracion:
    python3 src/migrate.py

### correr flask:
    flask run

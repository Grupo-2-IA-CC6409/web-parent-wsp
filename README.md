## Parte web del proyecto para el curso `Taller de Desarrollo de Proyectos de IA`

### Dev setup
Primero hay que tener instalado Python, se puede checkear con
```sh
python3 --version
```
Luego se deber crear el ambiente virtual, para eso corremos lo siguiente
```sh
python3 -m venv venv
```
Ahora debemos activar este ambiente con
```sh
source venv/bin/activate
```
e instalamos las dependecias
```sh
pip3 install -r requirements.txt
```
Ahora debemos copiar y modificar como sea necesario `example.env` en `.env`
```sh
cp example.env .env
```
Por ultimo para instalar [pre-commit](https://pre-commit.com)
```sh
./install-pre-commit.sh
```

### Correr el proyecto
Una vez hecho el setup y estando el ambiente virtual activado debemos aplicar las 
migraciones a la base de datos, esto se hace con
```sh
python3 manage.py migrate
```
y luego para correr el servidor se hace con
```sh
python3 manage.py runserver
```

# coding=utf-8
# Archivo que inicializa las variables globales para que se puedan acceder desde los templates

# Se importa la librería requests para manejar peticiones GET
from requests import get

"""
   Método que hace una petición inicial a los servicios y establece con los resultados las variables globales
   para ser usadas en los templates
"""
def set_globals(app):
	cl1= get('http://104.131.16.36')
	rdm= get('http://104.131.59.50')
	cl2= get('http://104.131.90.195')
	cl3= get('http://104.131.93.15')

	if cl1.status_code==200:
		app.jinja_env.globals.update(cl1=cl1.content)
		app.jinja_env.globals.update(st_1=1)
	else:
		app.jinja_env.globals.update(cl1="null")
		app.jinja_env.globals.update(st_1=0)

	if rdm.status_code==200:
		app.jinja_env.globals.update(rdm=rdm.content)
		app.jinja_env.globals.update(st_2=1)
	else:
		app.jinja_env.globals.update(cl1="'null'")
		app.jinja_env.globals.update(st_2=0)

	if cl2.status_code==200:
		app.jinja_env.globals.update(cl2=cl2.content)
		app.jinja_env.globals.update(st_3=1)
	else:
		app.jinja_env.globals.update(cl1="'null'")
		app.jinja_env.globals.update(st_3=0)

	if cl3.status_code==200:
		app.jinja_env.globals.update(cl3=cl3.content)
		app.jinja_env.globals.update(st_4=1)
	else:
		app.jinja_env.globals.update(cl1="'null'")
		app.jinja_env.globals.update(st_4=0)
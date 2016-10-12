# coding=utf-8
# Archivo que inicializa las variables globales para que se puedan acceder desde los templates

# Se importa la librería requests para manejar peticiones GET
from requests import get
import serviceconfig

"""
   Método que hace una petición inicial a los servicios y establece con los resultados las variables globales
   para ser usadas en los templates
"""
def set_globals(app):
	services= serviceconfig.get_services()

	url_1= services['service_1']['host']
	url_2= services['service_2']['host']
	url_3= services['service_3']['host']
	url_4= services['service_4']['host']

	cl1= get(url_1)
	rdm= get(url_2)
	cl2= get(url_3)
	cl3= get(url_4)
	
	app.jinja_env.globals.update(url_1=url_1)
	app.jinja_env.globals.update(url_2=url_2)
	app.jinja_env.globals.update(url_3=url_3)
	app.jinja_env.globals.update(url_4=url_4)

	app.jinja_env.globals.update(desc_1=unicode(services['service_1']['description'],'utf-8'))
	app.jinja_env.globals.update(desc_2=unicode(services['service_2']['description'],'utf-8'))
	app.jinja_env.globals.update(desc_3=unicode(services['service_3']['description'],'utf-8'))
	app.jinja_env.globals.update(desc_4=unicode(services['service_4']['description'],'utf-8'))

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
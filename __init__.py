# coding=utf-8
# Archivo principal de la aplicación. Se inicializan los otros archivos necesarios

# Se importan los módulos flask: para correr la aplicación; globals para establecer las globales y servicemonitor para 
# iniciar el monitoreo de los servicios
from flask import Flask, render_template
import globals
import servicemonitor

# Variable que representa la aplicación.
app= Flask(__name__)

global rt1, rt2, rt3, rt4

# Se llama el método set_globals del módulo globals para establecer las variables globales
globals.set_globals(app)
rt1= globals.rt1
rt2= globals.rt2
rt3= globals.rt3
rt4= globals.rt4

# Se llama el método set_services de servicemonitor para cargar la información de los servicios
servicemonitor.set_services()

# Se llama el método run_monitor de servicemonitor para iniciar el monitoreo de servicios
servicemonitor.run_monitor()

"""
	Se define una ruta para el índice de la aplicación
"""
@app.route('/')
def homepage():
	return render_template("main.html")

@app.route('/service1')
def service_1():
	return servicemonitor.get_rt(0)

@app.route('/service2')
def service_2():
	return servicemonitor.get_rt(1)

@app.route('/service3')
def service_3():
	return servicemonitor.get_rt(2)

@app.route('/service4')
def service_4():
	return servicemonitor.get_rt(3)

@app.route('/lista')
def lista():
	return str(servicemonitor.get_rtt())
"""
	Método equivalente al Main. Inicia la aplicación
"""
if __name__== "__main__":
	app.run()

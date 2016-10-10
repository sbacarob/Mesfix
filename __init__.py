# coding=utf-8
# Archivo principal de la aplicación. Se inicializan los otros archivos necesarios

# Se importan los módulos flask: para correr la aplicación; globals para establecer las globales y servicemonitor para 
# iniciar el monitoreo de los servicios
from flask import Flask, render_template
import globals
import servicemonitor

# Variable que representa la aplicación.
app= Flask(__name__)

# Se llama el método set_globals del módulo globals para establecer las variables globales
globals.set_globals(app)

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

"""
	Método equivalente al Main. Inicia la aplicación
"""
if __name__== "__main__":
	app.run()

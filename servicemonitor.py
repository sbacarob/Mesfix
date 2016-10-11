# coding=utf-8
# Este módulo se encarga de iniciar las peticiones GET asíncronas minuto a minuto. Toma la información del archivo de
# configuración de servicios. También se encarga de reestablecer los servicios en caso de que fallen

# Se importan las librerías request: para manejo de peticiones GET; serviceconfig: para tener acceso a los servidores
# configurados en dicho módulo; paramiko: para manejo de conexiones SSH; y el módulo Timer de threading para hacer una función periódicamente
import requests
import serviceconfig
import paramiko
from threading import Timer

""" Diccionario que almacena los servicios"""
services={}

"""
	Método que carga los servicios del archivo de configuración de servicios.
	Inicializa el diccionario de servicios con los cargados
"""
def set_services():
	global services
	services=serviceconfig.get_services()
	print "Services were set"

"""
	Método que evalúa el estado de un servicio haciendo una petición GET al mismo
"""
def check_service(url,number,key):
	print "Entró en check_service con el número %s" %(number)
	req= requests.get(url)
	if req.status_code != 200:
		print "El servicio %s estaba caído. Devolvió un el código %s. Intentando reiniciar" %(number,req.status_code)
		restart_service(key)
	else:
		print "El servicio %s está funcionando correctamente" %(number)

"""
	Método que inicia el monitoreo. Tiene un temporizador que es llamado antes de correr nuevamente el método.
"""
def run_monitor():
	print "Entró en run monitor"
	ind=1
	for service in services:
		check_service(services[service]['url'],ind,service)
		ind+=1
	t= Timer(60,run_monitor) # Se declara el temporizador para correr la función run_monitor en 60 segundos
	t.start() # Se inicia el temporizador

"""
	Método que se encarga de reiniciar un servicio dada su llave dentro del diccionario de servicios.
	El parámetro key es la llave.
	El método reinicia el servidor en el que corre el servicio 
"""
def restart_service(key):
	print "Intentando reiniciar el servicio"
	ssh= paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(services[key]['ip'],username=services[key]['user'],password=services[key]['pass'])
	stdin, stdout, stderr = ssh.exec_command("sudo reboot")
	stdin.write(services[key]['pass']+'\n')
	stdin.flush()
	ssh.close()
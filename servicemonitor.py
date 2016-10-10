# coding=utf-8
import requests
import serviceconfig
from threading import Timer

services={}

def set_services():
	global services
	services=serviceconfig.get_services()
	print "Services were set"

def check_service(url,number):
	print "Entró en check_service con el número %s" %(number)
	req= requests.get(url)
	if req.status_code != 200:
		print "El servicio %s estaba caído. Intentando reiniciar" %(number)
		restart_service(url)
	else:
		print "El servicio %s está funcionando correctamente" %(number)

def run_monitor():
	print "Entró en run monitor"
	ind=1
	for service in services:
		check_service(services[service]['url'],ind)
		ind+=1
	t= Timer(60,run_monitor)
	t.start()


def restart_service():
	print "Intentando reiniciar el servicio"
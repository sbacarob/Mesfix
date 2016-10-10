# coding=utf-8
import requests
import serviceconfig
import paramiko
from threading import Timer

services={}

def set_services():
	global services
	services=serviceconfig.get_services()
	print "Services were set"

def check_service(url,number,key):
	print "Entró en check_service con el número %s" %(number)
	req= requests.get(url)
	if req.status_code != 200:
		print "El servicio %s estaba caído. Devolvió un el código %s. Intentando reiniciar" %(number,req.status_code)
		restart_service(key)
	else:
		print "El servicio %s está funcionando correctamente" %(number)

def run_monitor():
	print "Entró en run monitor"
	ind=1
	for service in services:
		check_service(services[service]['url'],ind,service)
		ind+=1
	t= Timer(60,run_monitor)
	t.start()


def restart_service(key):
	print "Intentando reiniciar el servicio"
	if services[key]['tipo']==serviceconfig.LINUX:
		ssh= paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(services[key]['ip'],username=services[key]['user'],password=services[key]['pass'])
		stdin, stdout, stderr = ssh.exec_command("sudo reboot")
		stdin.write(services[key]['pass']+'\n')
		stdin.flush()
		ssh.close()
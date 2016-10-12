# coding=utf-8

user='root'
passwd='!prueba-mesfix-12345'

# Diccionario en el que se declaran los servicios. 
# Estos servicios serán utilizados para inicializar el monitoreo desde el servidor
services={
	'service_1':{
		'host':'http://104.131.16.36',
		'user':user,
		'pass':passwd,
		'description':'Monitoreo del clima de Bogotá'
	},
	'service_2':{
		'host':'http://104.131.59.50',
		'user':user,
		'pass':passwd,
		'description':'Números aleatorios'
	},
	'service_3':{
		'host':'http://104.131.90.195',
		'user':user,
		'pass':passwd,
		'description':'Monitoreo del clima de Manizales'
	},
	'service_4':{
		'host':'http://104.131.93.15',
		'user':user,
		'pass':passwd,
		'description':'Monitoreo del clima de Chigorodó'
	}
}

"""
	Método que devuelve el diccionario de servicios declarado anteriormente
"""
def get_services():
	return services

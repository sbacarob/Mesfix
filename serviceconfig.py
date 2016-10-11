# coding=utf-8

# Diccionario en el que se declaran los servicios. 
# Estos servicios serán utilizados para inicializar el monitoreo desde el servidor
services={
	'service_1':{
		'url':'http://mt-ds1.herokuapp.com',
		'user':'sbacarob@outlook.com',
		'ip':'174.129.199.201',
		'pass':''
	},
	'service_2':{
		'url':'http://mt-ds2.herokuapp.com',
		'user':'sbacarob@outlook.com',
		'ip':'54.235.116.11',
		'pass':''
	},
	'service_3':{
		'url':'http://mt-ds3.herokuapp.com',
		'user':'sbacarob@outlook.com',
		'ip':'54.235.116.11',
		'pass':''
	},
	'service_4':{
		'url':'http://mt-ds4.herokuapp.com',
		'user':'sbacarob@outlook.com',
		'ip':'54.235.116.11',
		'pass':''
	}
}

"""
	Método que devuelve el diccionario de servicios declarado anteriormente
"""
def get_services():
	return services

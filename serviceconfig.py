# coding=utf-8

# Constante para un servicio corriendo en un servidor Linux
LINUX='Linux'

# Constante para un servicio corriendo en nun servidor Heroku
HEROKU='Heroku'

services={
	'service_1':{
		'tipo': HEROKU,
		'url':'http://mt-ds1.herokuapp.com',
		'user':'sbacarob@outlook.com',
		'pass':''
	},
	'service_2':{
		'tipo': HEROKU,
		'url':'http://mt-ds1.herokuapp.com',
		'user':'sbacarob@outlook.com',
		'pass':''
	},
	'service_3':{
		'tipo': HEROKU,
		'url':'http://mt-ds1.herokuapp.com',
		'user':'sbacarob@outlook.com',
		'pass':''
	},
	'service_4':{
		'tipo': HEROKU,
		'url':'http://mt-ds1.herokuapp.com',
		'user':'sbacarob@outlook.com',
		'pass':''
	}
}

def get_services():
	return services

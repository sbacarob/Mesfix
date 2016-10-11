# Mesfix
## Prueba Mesfix

Monitor de estado de servicios hecho en python utilizando Flask, que realiza peticiones get a URLs de algún host que devuelva una respuesta numérica sencilla. Se muestra una gráfica de la respuesta numérica que se actualiza cada minuto y un indicador de si el servidor está corriendo o está caído.

### Librerías de python requeridas para correr la aplicación:

- requests
- paramiko
- threading
- flask

### Correr la aplicación:

Para correr la aplicación se debe ejecutar en la consola de comandos desde el directorio raíz:

```
$ export FLASK_APP=__init__.py
$ flask run
```

### Configuración de servicios:

En el archivo `serviceconfig.py` ubicado en el directorio raíz hay un diccionario llamado services, que tiene la siguiente estructura

```
services={
	'service_1':{ # Las llaves son identificadores de cada servicio. Cada servicio es un diccionario
		'host':'104.131.16.36', # La dirección IP donde está hosteado el servicio 
		'user':'user@host', # El usuario con el cual se va a conectar al servidor
		'pass':'' # Contraseña para conectarse al servidor y ejecutar los comandos bash
	},
	'service_2':{
		'host':'104.131.90.195',
		'user':'user@host',
		'pass':''
	}
}
```
### Capturas de pantalla

Aquí se muestra un ejemplo con tres servicios funcionales y uno caído:

![alt text](https://github.com/sbacarob/Mesfix/blob/master/mesfix2.png "Screenshot 1")

Cuando un servicio se cae, la aplicación intenta reestablecerlo automáticamente mediante un comando bash. Aún así, se puede enviar una petición desde el lado del cliente haciendo click en el ícono de la llave

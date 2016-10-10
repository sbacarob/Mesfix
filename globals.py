from requests import get

def set_globals(app):
	cl1= get('http://mt-ds1.herokuapp.com')
	rdm= get('http://mt-ds2.herokuapp.com')
	cl2= get('http://mt-ds3.herokuapp.com')
	cl3= get('http://mt-ds4.herokuapp.com')

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
from requests import get

cl1= get('http://mt-ds1.herokuapp.com').content
rdm= get('http://mt-ds2.herokuapp.com').content
cl2= get('http://mt-ds3.herokuapp.com').content
cl3= get('http://mt-ds4.herokuapp.com').content

def set_globals(app):
	app.jinja_env.globals.update(cl1=cl1)
	app.jinja_env.globals.update(rdm=rdm)
	app.jinja_env.globals.update(cl2=cl2)
	app.jinja_env.globals.update(cl3=cl3)
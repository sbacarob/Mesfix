from flask import Flask, render_template
from requests import get

app= Flask(__name__)

app.jinja_env.globals.update(get=get)

cl3= get('http://mt-ds4.herokuapp.com').content
app.jinja_env.globals.update(cl3=cl3)

@app.route('/')
def homepage():
	return render_template("main.html")


if __name__== "__main__":
	app.run()

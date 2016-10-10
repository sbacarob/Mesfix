from flask import Flask, render_template
import globals

app= Flask(__name__)
globals.set_globals(app)

@app.route('/')
def homepage():
	return render_template("main.html")


if __name__== "__main__":
	app.run()

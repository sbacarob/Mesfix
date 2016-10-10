# coding=utf-8
from flask import Flask, render_template
import globals
import servicemonitor

app= Flask(__name__)
globals.set_globals(app)
servicemonitor.set_services()
servicemonitor.run_monitor()

@app.route('/')
def homepage():
	return render_template("main.html")


if __name__== "__main__":
	app.run()

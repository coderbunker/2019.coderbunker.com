from flask import Flask, request, jsonify, url_for, redirect, render_template
import json

app = Flask(__name__, template_folder='./')

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/<path:anything>', methods=['GET'])
def public(anything):
	print(request.path)
	print(anything)
	return render_template(anything)

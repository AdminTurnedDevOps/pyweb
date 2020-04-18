from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap

pyweb = Flask(__name__)
Bootstrap(pyweb)

@pyweb.route("/")
def index():
    return render_template('index.html')

pyweb.run
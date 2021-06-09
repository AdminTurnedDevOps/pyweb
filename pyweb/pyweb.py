from flask import Flask, render_template, request, jsonify


pyweb = Flask(__name__)


@pyweb.route("/")
def home():
    return 'Hello, CloudDev Friends!'


pyweb.run()

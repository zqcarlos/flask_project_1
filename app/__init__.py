from flask import Flask
app = Flask(__name__)
app.config.from_objext('config')

from app import views


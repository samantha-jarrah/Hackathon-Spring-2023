from flask import Flask
from config import Config

backend = Flask(__name__)
backend.config.from_object(Config)

from backend import routes
from flask import Flask

from .api import app
from . import models

# Connect sqlalchemy to app
models.db.init_app(app)
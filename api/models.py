from flask_sqlalchemy import SQLAlchemy

from .api import app

import datetime

# Create database connection object
db = SQLAlchemy(app)

class CaptureCO2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.now())
    ppm = db.Column(db.Integer(), nullable=False)

    def __init__(self, date, ppm):
        self.date = date
        self.ppm = ppm

db.create_all()
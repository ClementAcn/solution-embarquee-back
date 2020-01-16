import flask
import sqlite3
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/data/<int:id>', methods=['GET'])
def send_data(id):
  #returns the post, the post_id should be an int
  co2 = request.args['co2']
  res = 'Carte n° ' + str(id) + '<br>co2 : ' + co2 + 'ppm'
  return res

app.run()
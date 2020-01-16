# Fichier de configuration
import os

SECRET_KEY = '\x8d\xfd\xcab\xcer\xccE\xdf\xd8\xfe\xf1\xe3\xa9\xd0\xee'

# Initialisation de la base de données
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
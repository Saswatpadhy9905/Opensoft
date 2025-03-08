import os

# Get the absolute path of the project directory.
basedir = os.path.abspath("C:\\Users\\sppad\\Desktop\\Chem Sem\\attempt2")

class Config:
    # Generate a secret key for security (you may use a fixed key in production)
    SECRET_KEY = os.urandom(24)
    # SQLAlchemy database URI – we store the SQLite database in the instance folder.
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance', 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Standard Libraries
import pathlib
import os

# External Libraries
import connexion
import flask
from flask_cors import CORS

# Internal Libraries
from .schemas.orm import init_db


# functions
def post_schemas():
    pass


def get_schemas(operationId):
    pass


def post_merge(operationIds):
    pass


# environment variables
DB_USER = os.environ['DB_USER']
DB_SERVER = os.environ['DB_SERVER']
DB_NAME = os.environ['DB_NAME']

# options
options = {'swagger_ui': False}

# create flask app
app = connexion.FlaskApp(__name__, port=9090, specification_dir='schemas/')
app.add_api('api.yml', strict_validation=True, options=options)
CORS(app.app)

# connect to database
init_db(uri=f'postgres+psycopg2://{DB_USER}@{DB_SERVER}:5432/{DB_NAME}')

from setuptools import setup, find_packages


APP_NAME = 'srs'
VERSION = '0.1.0'
AUTHOR = 'James Hibbard'

setup(
    name=APP_NAME,
    version=VERSION,
    author=AUTHOR,
    description='Schema Registry Server',
    license='MIT',
    install_requires=[
        'Flask==1.0.2',
        'connexion==2.0.2',
        'Flask-Cors==3.0.7',
        'SQLAlchemy==1.2.14',
        'gunicorn==19.9.0',
        'psycopg2-binary==2.7.6.1',
        'Flask-Cors==3.0.7',
    ],
    packages=find_packages(),
)

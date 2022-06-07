from setuptools import setup, find_packages

setup(
    name='skygrid',
    version='0.1.20',
    url='https://github.com/skygrid/skygrid-api-server',
    author='Alexander Baranov',
    author_email='sashab1@yandex-team.ru',
    packages=find_packages(),
    description='SkyGrid API server',
    install_requires=[
        "Flask",
        "Flask-RESTful",
        "Jinja2",
        "MarkupSafe",
        "WTForms",
        "aniso8601",
        "argparse",
        "flask-mongoengine",
        "itsdangerous",
        "mongoengine",
        "pymongo",
        "pytz",
        "requests",
        "six",
        "wsgiref",
        "pika",
        "skygrid-libscheduler",
        "flask-cors",
        "gevent"
    ],
    tests_require=[
        "nose",
        "nose-testconfig",
    ],
)

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
        "Flask>=0.10.1",
        "Flask-RESTful==0.2.12",
        "Jinja2",
        "MarkupSafe==0.23",
        "WTForms==2.0.1",
        "Werkzeug==0.9.6",
        "aniso8601==0.83",
        "argparse==1.2.1",
        "flask-mongoengine>=0.7.1",
        "itsdangerous==0.24",
        "mongoengine==0.8.7",
        "pymongo==2.7.2",
        "pytz==2014.4",
        "requests",
        "six==1.7.3",
        "wsgiref==0.1.2",
        "pika==0.9.14",
        "skygrid-libscheduler==0.5.5",
        "flask-cors",
        "gevent"
    ],
    tests_require=[
        "nose==1.3.4",
        "nose-testconfig==0.9",
    ],
)

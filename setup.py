from os.path import abspath, dirname, join, normpath

from setuptools import setup


setup(

    # Basic package information:
    name = 'Flask-Heroku-RQify',
    version = '0.1',
    py_modules = ('flask_rqify', ),

    # Packaging options:
    zip_safe = False,
    include_package_data = True,

    # Package dependencies:
    install_requires = [
        'Flask-RQ==0.2',
        'Flask-Script>=0.5.3',
    ],

    # Metadata for PyPI:
    author = 'Randall Degges',
    author_email = 'rdegges@gmail.com',
    license = 'UNLICENSE',
    url = 'https://github.com/rdegges/flask-heroku-cacheify',
    keywords = 'flask heroku cloud cache memcache memcached redis awesome',
    description = 'Automatic RQ configuration for your Heroku Flask applications.',
    long_description = open(normpath(join(dirname(abspath(__file__)),
        'README.md'))).read()

)

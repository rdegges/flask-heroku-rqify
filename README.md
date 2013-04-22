# flask-heroku-rqify

Automatic RQ configuration for your Heroku Flask applications.

![Worker Sketch](https://raw.github.com/rdegges/flask-heroku-rqify/master/assets/worker-sketch.jpg)


## Purpose

[RQ](http://python-rq.org/) is a lightweight, simple, and efficient Python
library for queueing jobs and processing them in the background with workers.
It uses [Redis](http://redis.io/) as a back end.

`flask-heroku-rqify` handles all RQ configuration for you, so that you can get
your application processing asynchronous tasks with only a single line of code!

In addition to make configuration easier, `flask-heroku-rqify` also allows you
to seamlessly switch your Heroku Redis provider instantly, with no downtime.  By
analyzing which Redis addons your Heroku application has available, and
automatically configuring RQ to use these addons, you can easily swap your Redis
providers around without touching a single line of code!


## Install

To install `flask-heroku-rqify`, use [pip](http://pip.readthedocs.org/en/latest/).

```bash
$ pip install flask-heroku-rqify
```

Next, modify your `requirements.txt` file in your home directory, and add the
following to the bottom of your file:

```bash
Flask-Heroku-RQify>=0.1
```


## Pick an Addon

Heroku has lots of available Redis addons.  `flask-heroku-rqify` works with
them all!  That means no matter which option you choose, your queue will work
out of the box, guaranteed!

Below is a list of the addons you can install to get started, you should have at
least one of these activated on your Heroku app -- otherwise,
`flask-heroku-rqify` will attempt to connect to your default Redis instance
running locally (good for local development).

- [RedisGreen](https://addons.heroku.com/redisgreen)
- [MyRedis](https://addons.heroku.com/myredis)
- [Redis Cloud](https://addons.heroku.com/rediscloud)
- [Redis To Go](https://addons.heroku.com/redistogo)
- [openredis](https://addons.heroku.com/openredis)

**NOTE**: My favorite providers are openredis and RedisGreen.


## Usage

Using `flask-heroku-rqify` is *super easy*!  In your `app.py` (or wherever
you define your Flask application), add the following:

```python
from flask.ext.rqify import init_rqify

app = Flask(__name__)
init_rqify(app)
```

To define tasks, you can do the following:

```python
from flask.ext.rq import job

@job
def process(i):
    # process stuff...
```

To use the task defined above, you could do:

```python
>>> process.delay(2)
```

Once you've defined your tasks, it's now time to boot up a worker process!  To
do this, we'll use the
[Flask-Script](http://flask-script.readthedocs.org/en/latest/) extension (which
is installed automatically by `flask-heroku-rqify`).  In your project directory,
create a new file named `manage.py`, and add the following:

```python
from flask.ext.rq import get_worker
from flask.ext.script import Manager

from myapp import app


manager = Manager(app)


@manager.command
def work():
    """Process the queue."""
    get_worker().work()


if __name__ == '__main__':
    manager.run()
```

Then modify your `Procfile`, and add the following line:

```
worker: python manage.py work
```

Now, to start processing your tasks on your new worker, you can finally just
spin up a new worker process using `heroku scale`:

```bash
$ heroku scale worker=1
```

If you'd like to process your queue faster, you can add more workers at any
time:

```bash
$ heroku scale worker=10
```

How does this work?  In the background, `flask-heroku-rqify` is really just
automatically configuring the popular
[Flask-RQ](https://flask-rq.readthedocs.org/en/latest/) extension!  This means,
you can basically read through the [official
documentation](https://flask-rq.readthedocs.org/en/latest/) to learn more about
RQ, how it works, and how Flask-RQ works.


## Like This?

Like this software?  If you really enjoy `flask-heroku-rqify`, you can show
your appreciation by:

- Sending me some bitcoin, my address is: **166UZk46Y6sLBj2br1whB9mvzxQD2EVfUp**
- Tipping me on [gittip](https://www.gittip.com/rdegges/).

Either way, thanks!  <3


## Changelog

v0.1: 04-21-2013

    - Pushing first release to PyPI!
    - Adding `init_rqify` handler to auto-configure Flask-RQ.

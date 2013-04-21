from os import environ

from flask.ext.rq import RQ


def init_rqify(app):
    """Auto-configure an appropriate Redis service for your Flask application.

    :param app app: Your Flask application.
    """
    # Look for RedisGreen.
    if any([k.startswith('REDISGREEN_') for k in environ]):
        app.config.setdefault('RQ_DEFAULT_URL', environ.get('REDISGREEN_URL'))

    # Look for MyRedis.
    elif any([k.startswith('MYREDIS_') for k in environ]):
        app.config.setdefault('RQ_DEFAULT_URL', environ.get('MYREDIS_URL'))

    # Look for Redis Cloud.
    elif any([k.startswith('REDISCLOUD_') for k in environ]):
        app.config.setdefault('RQ_DEFAULT_URL', environ.get('REDISCLOUD_URL'))

    # Look for Redis To Go.
    elif any([k.startswith('REDISTOGO_') for k in environ]):
        app.config.setdefault('RQ_DEFAULT_URL', environ.get('REDISTOGO_URL'))

    # Look for openredis.
    elif any([k.startswith('OPENREDIS_') for k in environ]):
        app.config.setdefault('RQ_DEFAULT_URL', environ.get('OPENREDIS_URL'))

    RQ(app)

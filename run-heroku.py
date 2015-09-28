#!/usr/bin/env python
from os import environ

# Port given by Heroku
_PORT = environ['PORT']


def run_tornado():
    # Script for running in Heroku
    from tornado.wsgi import WSGIContainer
    from tornado.httpserver import HTTPServer
    from tornado.ioloop import IOLoop
    from app import app

    import logging
    from logging import StreamHandler

    file_handler = StreamHandler()
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)

    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(_PORT)
    IOLoop.instance().start()

run_tornado()

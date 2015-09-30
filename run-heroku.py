#!/usr/bin/env python
from os import environ
from app import app

# Port given by Heroku
PORT = environ['PORT']


def run_tornado():
    # TODO More robust server.
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
    http_server.listen(PORT)
    print("Start serving")
    IOLoop.instance().start()


def run_flask():
    print("Start serving")
    app.run(host='0.0.0.0', port=PORT, debug=False)

run_flask()

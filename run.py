#!/bin/bash/python

from webapp.app import app

if __name__ == '__main__':
    app.run(use_reloader=True)
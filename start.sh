#!/bin/bash

export SECRET_KEY="z+xJ2JKT6R16"
export APP_SETTINGS="config.DevelopmentConfig"

gunicorn -w 3 -b :5000 -t 30 --reload run:app

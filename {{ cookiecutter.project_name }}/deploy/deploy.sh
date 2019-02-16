#!/bin/bash

set -e

eval $(docker-machine env {{ cookiecutter.domain }})

docker-compose up --build -d

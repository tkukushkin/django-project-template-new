#!/bin/bash

set -e

ssh root@{{ cookiecutter.domain }} bash -c '
  set -e
  apt-get update
  apt-get install -y socat apt-transport-https ca-certificates curl gnupg-agent software-properties-common
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
  add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
  apt-get update
  apt-get install -y docker-ce docker-ce-cli containerd.io
  [ ! -d .acme.sh ] && curl https://get.acme.sh | sh
  ./.acme.sh/acme.sh --issue --standalone -d {{ cookiecutter.domain }} --force
  mkdir -p certs
  ./.acme.sh/acme.sh --install-cert -d {{ cookiecutter.domain }} --cert-file certs/cert.pem --key-file certs/key.pem --fullchain-file certs/fullchain.pem
  mkdir -p media
'

[ -z $(docker-machine ls --filter 'NAME={{ cookiecutter.domain }}' -q) ] && docker-machine create --driver generic --generic-ip-address={{ cookiecutter.domain }} --generic-ssh-user=root --generic-ssh-key ~/.ssh/id_rsa {{ cookiecutter.domain }}

./deploy/deploy.sh

ssh root@{{ cookiecutter.domain }} bash -c '
  set -e
  ./.acme.sh/acme.sh --remove -d {{ cookiecutter.domain }}
  mkdir -p acme-challenges
  ./.acme.sh/acme.sh --issue -d {{ cookiecutter.domain }} -w acme-challenges/
'

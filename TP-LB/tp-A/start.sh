#!/bin/bash

# Créer le réseau
docker network create tplb

# Construire l'image de load balancer
docker build -t im-nginx-lb .

# Créer les dossiers partagés
mkdir -p shared1 shared2

# Créer les fichiers index.html
echo "<h1>Hello 1</h1>" > shared1/index.html
echo "<h1>Hello 2</h1>" > shared2/index.html

# Lancer les conteneurs nginx avec le bind mount
docker run --rm -d --name nginx1 --network tplb -p 81:80 -v $(pwd)/shared1:/usr/share/nginx/html nginx:latest

docker run --rm -d --name nginx2 --network tplb -p 82:80 -v $(pwd)/shared2:/usr/share/nginx/html nginx:latest

# Lancer le conteneur de load balancer
docker run --rm -d --name nginx-lb --network tplb -p 83:80 im-nginx-lb


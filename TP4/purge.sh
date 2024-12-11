#!/bin/bash
docker kill $(docker ps -q)
docker rm $(docker ps -aq)

docker network prune -f
docker volume prune -f


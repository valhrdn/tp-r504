#!/bin/bash

iter=0
oldnb=0

$TERM -t PRODUCER -e ./producer.sh &

while :
do
    nb=$(redis-cli LLEN mafile)
    iter=$((iter + 1))

    echo "-iter $iter, taille liste=$nb"

    if [ $nb -gt $oldnb ]; then
        ./consumer.sh &
    fi

    oldnb=$nb
    sleep 3
done


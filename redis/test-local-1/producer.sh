#!/bin/bash

while :
do
    for ((i=0;i<1000;i++))
    do
        redis-cli LPUSH mafile $RANDOM >/dev/null
    done
    redis-cli LLEN mafile
    sleep 3
done


#!/bin/bash

threshold=30000
delay_process=4

while :
do
    nb=$(redis-cli --raw LLEN mafile)
    if [ $nb -gt 0 ]; then
        value=$(redis-cli --raw RPOP mafile)
        echo "Consommé: $value"
        if [ $value -gt $threshold ]; then
            echo "ALARME! Valeur au-dessus du seuil: $value"
            sleep $delay_process
        fi
    else
        echo "Liste vide, attente 2s."
        sleep 2
    fi
done


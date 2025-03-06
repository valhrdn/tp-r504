#!/bin/bash

nmap -T4 172.16.0.0/24 > out

awk '/Nmap scan report/{ip=$5} /open/{ports=(ports?ports";":"")$1} /^$/{if(ip) print ip "," ports; ip=""; ports=""}' out > scan-result_1.csv


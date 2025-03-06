#!/bin/bash

nmap -T4 -sSU 172.16.0.0/24 > out2

awk '
/Nmap scan report/{ip=$5} 
/TCP open/{tcp_ports=(tcp_ports?tcp_ports";":"")$1} 
/UDP open/{udp_count++} 
/^$/{if(ip) print ip "," tcp_ports "," (udp_count?udp_count:0); ip=""; tcp_ports=""; udp_count=0}' out2 > scan-result_2.csv


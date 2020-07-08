#!/bin/bash
airmon-ng check kill
rfkill unblock all
ifconfig wlan0 down
iwconfig wlan0 mode monitor
ifconfig wlan0 up
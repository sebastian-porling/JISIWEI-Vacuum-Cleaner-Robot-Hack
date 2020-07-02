#!/bin/bash
ifconfig wlan0 down
iwconfig wlan0 mode Auto
ifconfig wlan0 up
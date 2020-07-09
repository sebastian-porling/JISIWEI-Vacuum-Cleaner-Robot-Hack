# JISIWEI Vacuum Cleaner Robot Demo
Created: 2020-06-29

Revised: 2020-07-08

This project consists of resources and documentation needed for re-creating and to demo the hack for the JISIWEI Vacuum Cleaner Robot at the NSE Cyber Security Lab. 

This demo will be based upon the HTTP vulnerability found in [CVE-2019-12820](https://www.cvedetails.com/cve/CVE-2019-12820/).

## Tools Used
- **Android Smartphone**, with the JISIWEI application installed
- **USB cable**, for connecting smarphone to PC
- **scrcpy**, for showing the Android screen on the PC
- **Aircrack-ng**, for cracking the wifi-password
- **nmap**, used for finding devices in network
- **arpspoof**, needed for transparant proxy
- **mitmproxy**, proxy used for looking at HTTP packets
- **Wireless Network Adapter**, needed for cracking the wifi and connecting to wifi
- **Wireless Router**, with relatively easy password for dictionary attack
- **JISIWEI Vacuum Cleaner Robot**

The computer **Dell OptiPlex 7070** should have everything installed. If you use the **TP-Link High-Gain 150Mbps** wireless adapter, you won't have to install any necessary drivers.

## QR HACK
The python script **qr_hack.py** is able to add **all** devices to the account **hackmanhacker8@gmail.com**. It is possible to change the account, you will have to get the variables **sign**, **state** and **time** in order to make the login POST HTTP request. 

The script has a **if statement** that will only make the HTTP request to add a device on the ID of the robot in the lab. Don't remove this **if statement**. Otherwise you would add all the existing robots to the account.

This QR code vulnerability is based on the [CVE-2019-12821](https://www.cvedetails.com/cve/CVE-2019-12821/).
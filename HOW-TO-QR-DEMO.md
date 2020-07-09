# HOW TO QR DEMO

## Setup
So in order to the robot in the lab it has to be unbinded from the account, this is done by doing the following:

1. Login to the account using the JISIWEI application
2. Press the "Menu button" on the left side of the screen
3. Choose "Device Manager"
4. Press "Unbind a device"

The robot should now be unbinded from the account and you could just run the script and the robot should be added under the name **PY**. You could change the name of the device by changing the variable **devname**. 

The python script requires the **requests** package, if it isn't already installed you will have to install it through **pip**:

```bash
pip install requests
```
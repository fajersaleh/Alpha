#!/bin/python
import subprocess

def discover_hosts():

    for i in range(1, 20):
        ip = "10.0.2." + str(i)

        result = subprocess.run(
            ["ping", "-c", "1", ip],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print(ip, "is Active")

discover_hosts()

import socket
target = input("Enter Target IP")
ports = [20,21,22,23,25,53,80,443,8080]
for port in ports:
    s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(1)
    
    result= s.connect_ex((target,port))
    if result == 0:
       print(f"Port{port}:OPEN")
    else:
       print(f"Port{port}:CLOSED")
    s.close()


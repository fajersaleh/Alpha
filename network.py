#!/usr/bin/env python3

import subprocess
import socket

# Network Discovery

def discover_hosts():
    print("Discovering devices...")

    for i in range(1, 20):
        ip = "10.0.2." + str(i)

        print(f"Checking {ip}...")

        result = subprocess.run(
            ["ping", "-c", "1", "-W", "1", ip],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print(ip, "is Active")


discover_hosts()

# Port Scanner

print("\nPORT SCANNER")

target = input("Enter Target IP: ")

ports = [20, 21, 22, 23, 25, 53, 80, 443, 8080]

print(f"\nScanning target: {target}")

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port}: OPEN")
    else:
        print(f"Port {port}: CLOSED")

    s.close()

print("Port scan completed.")

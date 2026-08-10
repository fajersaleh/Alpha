# Network Host Discovery and Port Scanner

## Overview

This project is a simple Python program for network discovery and TCP port scanning.

The program first finds active devices on the local network. After that, it scans selected TCP ports on the discovered hosts and shows which ports are open.

The project was tested in a controlled lab environment using Kali Linux.

## Features

- Finds active hosts on the local network.
- Uses Python sockets to check whether hosts are reachable.
- Scans selected TCP ports.
- Shows the IP address of discovered hosts.
- Shows the hostname of the target when available.
- Identifies common services based on port numbers.
- Saves scan results as CSV and TXT files.
- Creates a separate report for each scan.
- Includes an authorization check before starting the scan.

## Ports Scanned

The current program checks these TCP ports:

| Port | Common Service |
|------|----------------|
| 22   | SSH            |
| 80   | HTTP           |
| 443  | HTTPS          |

Port 8080 can also be added when testing with the lab server.

## Requirements

The project requires:

- Kali Linux
- Python 3

The program uses standard Python libraries:

- `socket`
- `csv`
- `os`
- `datetime`
- `concurrent.futures`

No additional Python packages are required.

## How to Run

Open a terminal in the project folder and run:

```bash
python3 network.py
```

The program first asks for authorization:

```text
Authorized to scan? (yes/no):
```

Enter:

```text
yes
```

to continue.

If the user enters anything other than `yes`, the scan will be cancelled.

## Network Discovery

After authorization, the program starts the network discovery stage.

The program gets the local IP address and uses the first three parts of the address to determine the local network range.

It then checks IP addresses from `.1` to `.254`.

For each address, the program tries to connect to port 80. If the connection is successful, the address is added to the list of discovered hosts.

Example:

```text
Discovering devices...
Found 3 device(s).
```

## Port Scanning

After finding the active hosts, the program starts the port scanning stage.

The current port list in `network.py` is:

```python
ports = [22, 80, 443]
```

For each discovered host, the program checks every port using a TCP socket.

If a connection is successful, the port is marked as `Open`.

The program also matches common port numbers with service names such as SSH, HTTP, and HTTPS.

## Test Server

A separate file called `vulnerable_server.py` can be used as a simple test server in the controlled lab environment.

If the test server is configured to listen on port 8080, add port 8080 to the list in `network.py` before testing:

```python
ports = [22, 80, 443, 8080]
```

This provides a controlled service that can be used to test the scanner.

To run the test server:

```bash
python3 vulnerable_server.py
```

## Reports

After the scan is completed, the program creates a `reports` folder if it does not already exist.

Two report files are generated:

```text
reports/scan_DATE_TIME.csv
reports/scan_DATE_TIME.txt
```

The CSV report contains:

- IP address
- Hostname
- Port
- Status
- Service

The TXT report contains the same information in a simple text format.

Example:

```text
NETWORK SCAN REPORT
========================================
Date: 2026-08-10 16:30:00
Open Ports: 2

IP: 10.0.2.15
Hostname: example
Port: 22
Status: Open
Service: SSH
------------------------------
```

## Project Files

```text
network.py
vulnerable_server.py
README.md
reports/
```

### network.py

This is the main program. It performs host discovery, port scanning, and creates the scan reports.

### vulnerable_server.py

This is the test server used in the controlled lab environment.

### README.md

This file explains the project and gives instructions for running and testing it.

### reports/

This folder contains the CSV and TXT files generated after a scan.

## Limitations

- The program checks the local network based on the IP address detected by the script.
- Host discovery depends on whether the target accepts the connection used by the program.
- Only the ports included in the `ports` list are checked.
- Service names are based on the port number.
- The scanner does not identify service versions.
- A port that does not accept the connection is treated as not open.
- Scan speed depends on the network and timeout settings.

## Responsible Use

This project is intended for learning and testing in a controlled environment.

Only scan networks and devices that you own or have permission to test. Do not use the program to scan external or unauthorized systems.

## Example Commands

Run the main program:

```bash
python3 network.py
```

Run the test server:

```bash
python3 vulnerable_server.py
```

Check the project files:

```bash
ls
```

## Conclusion

This project demonstrates basic network discovery and TCP port scanning using Python.

It shows how active hosts can be found, how selected ports can be checked, and how scan results can be saved as CSV and TXT files. The controlled test server also provides a safe way to test the scanner.

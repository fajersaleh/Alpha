# Network Host Discovery and Port Scanner

## Overview

This Python project performs basic network host discovery and TCP port scanning in a controlled lab environment.

The project consists of two main Python files:

1. **network.py** — discovers active hosts and scans selected TCP ports.
2. **vulnerable_server.py** — creates a simple TCP lab test server on port `8080` so the scanner can detect a known open port.

The project is intended for networking practice, cybersecurity education, and authorized lab testing.

---

## Features

- Discovers active hosts from `10.0.2.1` through `10.0.2.19`.
- Uses the system `ping` command for host discovery.
- Allows the user to enter a target IP address.
- Scans a predefined list of common TCP ports.
- Uses Python sockets and `connect_ex()` to test connections.
- Reports tested ports as `OPEN` or `CLOSED`.
- Uses a 1-second socket timeout.
- Includes a controlled TCP lab server running on port `8080`.
- Requires no third-party Python packages.

---

## Project Files

### `network.py`

The main scanner program. It performs two tasks:

- Network host discovery using ping requests.
- TCP port scanning against a user-selected target.

### `vulnerable_server.py`

A simple TCP test server used in the controlled lab environment.

The server:

- Listens on TCP port `8080`.
- Accepts incoming TCP connections.
- Displays the address of connecting clients.
- Sends a short welcome message.
- Closes the client connection after sending the message.
- Continues waiting for new connections.

Although the filename is `vulnerable_server.py`, it is used as a controlled **lab test server**. The current program demonstrates detection of an open service rather than exploitation of a software vulnerability.

---

## Ports Scanned

| Port | Common Service |
|------|----------------|
| 20 | FTP Data |
| 21 | FTP Control |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 443 | HTTPS |
| 8080 | Alternate HTTP / Lab Test Server |

Port `8080` is included so that `network.py` can detect the lab server during testing.

---

## Requirements

- Python 3
- Unix/Linux environment such as Kali Linux

The project uses only standard Python libraries:

- `subprocess`
- `socket`

No additional Python packages need to be installed.

---

## How to Run

### Step 1: Open the Project Folder

Open a terminal in the folder containing:

```text
network.py
vulnerable_server.py
README.md
```

### Step 2: Start the Lab Test Server

Open the first terminal and run:

```bash
python vulnerable_server.py
```

The server should display:

```text
===================================
       CYBERSECURITY LAB SERVER
===================================
Lab test server is running on port 8080
Waiting for connections...
-----------------------------------
```

Keep this terminal running.

### Step 3: Run the Network Scanner

Open a second terminal in the same project folder and run:

```bash
python network.py
```

The program first performs host discovery on:

```text
10.0.2.1 - 10.0.2.19
```

Example:

```text
10.0.2.5 is Active
10.0.2.10 is Active
```

After host discovery, the program asks:

```text
Enter Target IP:
```

For a simple test where the scanner and lab server are running on the same machine, enter:

```text
127.0.0.1
```

The scanner then checks the predefined TCP ports.

Example:

```text
Scanning target: 127.0.0.1
-----------------------------------
Port 20: CLOSED
Port 21: CLOSED
Port 22: CLOSED
Port 23: CLOSED
Port 25: CLOSED
Port 53: CLOSED
Port 80: CLOSED
Port 443: CLOSED
Port 8080: OPEN
-----------------------------------
Port scan completed.
```

Because the lab test server is running on port `8080`, the scanner should report:

```text
Port 8080: OPEN
```

The server terminal should also display a connection from the scanner.

---

## How It Works

### Host Discovery

The `discover_hosts()` function loops through IP addresses from:

```text
10.0.2.1
```

to:

```text
10.0.2.19
```

For each address, the program executes:

```bash
ping -c 1 <IP>
```

The `subprocess` library allows the Python program to execute the system ping command.

If the ping command completes successfully, the program displays the IP address as active.

---

## TCP Port Scanning

After host discovery, the user enters a target IP address.

For every port in the predefined list, `network.py`:

1. Creates an IPv4 TCP socket.
2. Sets a 1-second connection timeout.
3. Attempts to connect to the target port using `connect_ex()`.
4. Checks the returned result.
5. Displays `OPEN` if the connection succeeds.
6. Displays `CLOSED` if the connection does not succeed.
7. Closes the socket.
8. Continues to the next port.

A result of `0` from `connect_ex()` indicates that the TCP connection was successfully established.

---

## Lab Test Server

The `vulnerable_server.py` file provides a safe target for demonstrating the port scanner.

The server is configured with:

```text
Host: 0.0.0.0
Port: 8080
Protocol: TCP
```

The server creates an IPv4 TCP socket, binds it to port `8080`, and waits for incoming connections.

When the scanner connects to port `8080`, the server accepts the connection and sends:

```text
Welcome to the Cybersecurity Lab Test Server.

This server is used for testing the network port scanner.
```

The connection is then closed and the server continues waiting for another connection.

This provides a controlled way to verify that the scanner can correctly identify an open TCP port.

---

## Project Workflow

```text
Start
  |
  v
Run vulnerable_server.py
  |
  v
Server listens on port 8080
  |
  v
Run network.py
  |
  v
Discover active hosts
  |
  v
Enter target IP
  |
  v
Scan predefined TCP ports
  |
  v
Attempt TCP connections
  |
  v
Display OPEN / CLOSED results
  |
  v
Detect port 8080 lab server
  |
  v
End
```

---

## Current Limitations

- The discovery range is hard-coded to `10.0.2.1` through `10.0.2.19`.
- The TCP port list is predefined.
- Host discovery uses `ping -c 1`, which is intended for Unix/Linux systems.
- The program does not distinguish between closed and filtered ports.
- Service names and versions are not automatically identified.
- Results are displayed in the terminal and are not saved to a file.
- The scanner checks port availability but does not perform vulnerability detection.
- Firewalls and network configuration may affect discovery and scanning results.

---

## Future Improvements

Possible improvements include:

- Allowing the user to specify the network range.
- Allowing custom port ranges.
- Saving scan results to a text, CSV, or JSON file.
- Adding better error handling and input validation.
- Identifying services running on open ports.
- Creating a graphical user interface (GUI).
- Improving reporting and logging.

---

## Responsible Use

This project is intended for educational purposes and controlled lab testing.

Only scan systems and networks that you own or have explicit permission to test.

Unauthorized network scanning may violate organizational policies or applicable laws.

---

## Summary

This project demonstrates two fundamental networking concepts using Python: **host discovery and TCP port scanning**.

`network.py` identifies active hosts and checks selected TCP ports, while `vulnerable_server.py` provides a controlled TCP service on port `8080` for testing.

Together, the files demonstrate how Python's `subprocess` and `socket` libraries can be used to perform basic network discovery and TCP connectivity testing.

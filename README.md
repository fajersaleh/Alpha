# Network Host Discovery and Port Scanner

## Overview

This Python script performs two basic networking tasks:

1. **Host discovery** — it pings IP addresses from `10.0.2.1` through `10.0.2.19` and reports which hosts are active.
2. **TCP port scanning** — it asks the user for a target IP address and checks a predefined list of common TCP ports.

The script is intended for simple networking practice and controlled lab environments.

## Features

- Scans the subnet range `10.0.2.1` to `10.0.2.19`.
- Uses the system `ping` command to identify active hosts.
- Accepts a target IP address from the user.
- Checks common TCP ports using Python sockets.
- Reports each tested port as `OPEN` or `CLOSED`.
- Uses a 1-second socket timeout.

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

## Requirements

- Python 3
- Standard Python libraries:
  - `subprocess`
  - `socket`

No additional packages need to be installed.

## How to Run

Open a terminal in the folder containing the script and run:

```bash
python network.py
```

The script will first attempt to discover active hosts in the configured IP range.

Example output:

```text
10.0.2.5 is Active
10.0.2.10 is Active
```

After host discovery, the program asks:

```text
Enter Target IP
```

Enter the IP address you want to scan, for example:

```text
10.0.2.5
```

The program then checks the predefined ports and displays results similar to:

```text
Port22:OPEN
Port23:CLOSED
Port80:OPEN
Port443:CLOSED
```

## How It Works

### Host Discovery

The `discover_hosts()` function loops through IP addresses from `10.0.2.1` to `10.0.2.19`.

For each address, it sends one ping request:

```bash
ping -c 1 <IP>
```

If the ping command succeeds, the host is displayed as active.

### Port Scanning

After discovery, the script asks for a target IP address.

For every port in the predefined list, it:

1. Creates a TCP socket.
2. Sets a 1-second timeout.
3. Attempts a connection using `connect_ex()`.
4. Displays the port as `OPEN` when the connection succeeds.
5. Otherwise displays the port as `CLOSED`.
6. Closes the socket before testing the next port.

## Current Limitations

- The discovery range is hard-coded to `10.0.2.1` through `10.0.2.19`.
- The port list is hard-coded.
- The script uses `ping -c 1`, which is designed for Unix-like systems.
- A closed or filtered port may appear simply as `CLOSED`.
- Service versions are not identified.
- Results are printed to the terminal and are not saved to a file.

## Responsible Use

Use this script only on systems and networks that you own or have explicit permission to test.

Unauthorized network scanning may violate organizational policies or applicable laws.

## File

```text
network.py
```

This file contains both the host-discovery and TCP port-scanning logic.

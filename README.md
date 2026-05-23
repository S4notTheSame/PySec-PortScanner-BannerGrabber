# PySec Port Scanner & Banner Grabber

A small Python cybersecurity project for learning basic TCP port scanning and banner grabbing.

The tool scans selected TCP ports on a target IP address or hostname and attempts to collect basic service banners from open ports.

## Current Features

- Scans selected TCP ports on a target IP address or hostname
- Uses Python sockets for TCP connection checks
- Attempts basic banner grabbing on open ports
- Uses a command-line target argument
- Prints whether ports are open or closed/filtered
- Default tested ports: 21, 22, 25, 80, 110, 443, 3306

## Ethical Disclaimer

This tool is intended only for educational use and authorized testing.

Use it only on systems you own, administer, or have explicit permission to test. Unauthorized scanning may violate laws, policies, or terms of service.

## Requirements

Python 3.x

No external Python packages are required.

## Usage

Run the scanner by providing a target IP address or hostname:

```bash
python banner_grabber.py <target>


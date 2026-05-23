import socket

def scan_port(target, port):
     """
    Try to connect to one TCP port.
    If connect_ex() returns 0, the port is open.
    """
     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     sock.settimeout(2)

     result = sock.connect_ex((target, port))
     sock.close()

     if result == 0:
         return "open"
     else:
         return "closed/filtered"

target = input("Enter target IP: ")
ports = [21, 22, 25, 80, 110, 443, 3306]

for port in ports:
    status = scan_port(target, port)
    print(f"Port {port}: {status}")
import argparse
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

def grab_banner(target, port, timeout=2):
    """
    Try to grab a service banner from an open TCP port.

    Some services send a banner immediately.
    HTTP services usually require sending a request first.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((target, port))

        if port in [80, 8000, 8080]:
            request = f"HEAD / HTTP/1.1\r\nHost: {target}\r\nConnection: close\r\n\r\n"
            sock.sendall(request.encode())

        else:
            try:
                sock.send(b"\r\n")
            except OSError:
                pass

        banner = sock.recv(1024)
        sock.close()

        if banner:
            return banner.decode(errors="ignore").strip()
        else:
            return "No banner received"

    except socket.timeout:
        return "No banner received"
    except Exception as error:
        return f"Banner grab failed: {error}"


def main():
    parser = argparse.ArgumentParser(
        description="Basic TCP port scanner and banner grabber."
    )

    parser.add_argument(
        "target", help="The target IP address or hostname"
    )

    parser.add_argument(
        "--timeout",
        type=float,
        default=2,
        help="Timeout for socket connections. Default is 2 seconds."
    )

    args = parser.parse_args()

    ports = [21, 22, 25, 80, 110, 443, 3306]

    for port in ports:
        status = scan_port(args.target, port)

        if status == "open":
            banner = grab_banner(args.target, port)
            print(f"Port {port} ({status}) | Banner: {banner}")
        else:
            print(f"Port {port}: {status}")


if __name__ == "__main__":
    main()
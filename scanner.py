#!/usr/bin/env python3

import socket
import threading
import argparse
import time
from datetime import datetime

open_ports = []
lock = threading.Lock()

COMMON_SERVICES = {
    20: "FTP-DATA",
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    8080: "HTTP-ALT",
}


def scan_port(target_ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((target_ip, port))

        if result == 0:
            service = COMMON_SERVICES.get(port, "UNKNOWN")

            with lock:
                open_ports.append((port, service))

        sock.close()

    except Exception:
        pass


def scan_ports_range(target_ip, start_port, end_port):
    threads = []

    for port in range(start_port, end_port + 1):
        thread = threading.Thread(
            target=scan_port,
            args=(target_ip, port)
        )

        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def save_report(target, ip_address):
    filename = f"report_{target.replace('.', '_')}.txt"

    with open(filename, "w", encoding="utf-8") as report:
        report.write("PORT SCANNER REPORT\n")
        report.write("=" * 50 + "\n")
        report.write(f"Target: {target}\n")
        report.write(f"IP: {ip_address}\n")
        report.write(f"Generated: {datetime.now()}\n\n")

        if open_ports:
            report.write("OPEN PORTS\n")
            report.write("-" * 50 + "\n")

            for port, service in sorted(open_ports):
                report.write(
                    f"{port}/tcp\tOPEN\t{service}\n"
                )
        else:
            report.write("No open ports found.\n")

    print(f"\n[+] Report saved: {filename}")


def banner():
    print("=" * 50)
    print("         PYTHON PORT SCANNER")
    print("        Carlos Rodriguez")
    print("=" * 50)


def main():
    parser = argparse.ArgumentParser(
        description="Multithreaded Port Scanner"
    )

    parser.add_argument(
        "target",
        help="IP address or domain"
    )

    parser.add_argument(
        "start",
        type=int,
        help="Starting port"
    )

    parser.add_argument(
        "end",
        type=int,
        help="Ending port"
    )

    args = parser.parse_args()

    banner()

    try:
        target_ip = socket.gethostbyname(args.target)
    except socket.gaierror:
        print("[!] Unable to resolve target")
        return

    print(f"Target : {args.target}")
    print(f"IP     : {target_ip}")
    print(f"Ports  : {args.start}-{args.end}")

    start_time = time.time()

    scan_ports_range(
        target_ip,
        args.start,
        args.end
    )

    elapsed = time.time() - start_time

    print("\nScan Results")
    print("-" * 50)

    if open_ports:
        for port, service in sorted(open_ports):
            print(f"{port}/tcp\tOPEN\t{service}")
    else:
        print("No open ports found.")

    print(f"\nScan completed in {elapsed:.2f} seconds")

    save_report(args.target, target_ip)


if __name__ == "__main__":
    main()

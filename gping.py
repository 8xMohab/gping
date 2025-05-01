#!/usr/bin/env python3

import subprocess
import re
import signal
import sys

host = sys.argv[1] if len(sys.argv) > 1 else "google.com"
latencies = []

def handle_exit(signum, frame):
    print()  # newline after ^C
    if not latencies:
        print("No valid replies received.")
        sys.exit(1)

    min_latency = min(latencies)
    max_latency = max(latencies)
    avg_latency = sum(latencies) / len(latencies)

    print(f"---- {host} gping statistics ----")
    print(f"min = {min_latency:.2f} ms")
    print(f"avg = {avg_latency:.2f} ms")
    print(f"max = {max_latency:.2f} ms")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_exit)

# Run ping as a subprocess
with subprocess.Popen(
    ["ping", host],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True
) as proc:
    for line in proc.stdout:
        if "bytes from" in line and "time=" in line:
            # Extract IP (optional - from either (...) or raw)
            match_ip = re.search(r"\(([^)]+)\)", line)
            if match_ip:
                ip = match_ip.group(1)
            else:
                parts = line.split()
                ip = parts[3] if len(parts) > 3 else "?"

            # Extract latency
            match_time = re.search(r"time=([\d.]+)", line)
            if match_time:
                latency = float(match_time.group(1))
                latencies.append(latency)
                print(f"{ip} {latency:.1f} ms")

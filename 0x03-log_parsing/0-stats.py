#!/usr/bin/python3

"""A script that reads stdin lineby line and computes metrics"""

import sys
import signal

# Initialize metrics
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """Prints the log statistics of requests"""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def handle_interrupt(signum, frame):
    """Handles the CTRL+C command signal"""
    print_stats()
    sys.exit(0)

# Handle keyboard interrupt (CTRL + C)
signal.signal(signal.SIGINT, handle_interrupt)

for line in sys.stdin:
    try:
        parts = line.split()
        if len(parts) != 9:
            continue
        ip, dash, date, method, resource, protocol, status_code_str, file_size_str = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7]
        
        # Validate the format
        if dash != '-' or not date.startswith('[') or not date.endswith(']') or not method.startswith('"GET') or not protocol.endswith('"') or not resource.startswith('/projects/260'):
            continue
        
        # Parse status code and file size
        try:
            status_code = int(status_code_str)
            file_size = int(file_size_str)
        except ValueError:
            continue

        # Update metrics
        total_file_size += file_size
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        line_count += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

    except Exception:
        continue

# Print final stats at the end if less than 10 lines are processed
print_stats()

#!/usr/bin/python3

"""Log parser from stdin and computes metrics"""
import sys
import re
import signal


log_metadata: dict = {
    'line_count': 0,
    'total_file_size': 0,
    'status_code_count': {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
}


def print_statistics(log_metadata: dict):
    """Prints the log statistics of requests"""
    print("File size: {}".format(log_metadata['total_file_size']), flush=True)
    for stat_code, count in sorted(log_metadata['status_code_count'].items()):
        if count > 0:
            print("{}: {}".format(stat_code, count), flush=True)


def signal_handler(sig, frame):
    """Handles the CTRL+C command signal"""
    sys.exit(0)


# <IPAddress> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
LOG_PATTERN = re.compile(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) '
                         r'- \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\] '
                         r'"GET /projects/(\d+) HTTP/1\.1" (\d{3}) (\d+)$')


def read_input(log_metadata: dict):
    """Read api request logs and update the log metadata"""
    try:
        for line in sys.stdin:
            # Filter out logs that match the valid pattern
            matchedLog = re.match(LOG_PATTERN, line)

            # Keep track of valid logs only
            if matchedLog is not None:
                status_code = int(matchedLog.group(4))
                log_metadata['total_file_size'] += int(matchedLog.group(5))
                if status_code in log_metadata['status_code_count'].keys():
                    log_metadata['status_code_count'][status_code] += 1
            else:
                continue
            # Count the number of lines so far
            log_metadata['line_count'] += 1
            # Log statistics after every 10 requests
            if log_metadata['line_count'] % 10 == 0:
                print_statistics(log_metadata)
    finally:
        print_statistics(log_metadata)


# Registering signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

# Read logs piped inp and parse it
read_input(log_metadata)

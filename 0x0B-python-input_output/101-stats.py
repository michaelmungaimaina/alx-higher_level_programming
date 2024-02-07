#!/usr/bin/python3

import random
import sys
from time import sleep
import datetime

def generate_log_entries(num_entries=10000):
    """
    Generates synthetic log entries in the Combined Log Format and prints them to the standard output.

    Each log entry consists of an IP address, timestamp, HTTP request, status code, and response size.

    Args:
        num_entries (int): The number of log entries to generate. Defaults to 10,000.

    Returns:
        None
    """
    for i in range(num_entries):
        sleep(random.random())
        sys.stdout.write(
            '{:d}.{:d}.{:d}.{:d} - [{}] "GET /projects/260 HTTP/1.1" {} {}\n'.format(
                random.randint(1, 255),
                random.randint(1, 255),
                random.randint(1, 255),
                random.randint(1, 255),
                datetime.datetime.now(),
                random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
                random.randint(1, 1024),
            )
        )
        sys.stdout.flush()

if __name__ == "__main__":
    generate_log_entries()


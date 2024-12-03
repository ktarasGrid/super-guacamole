"""
This script analyzes an Apache access log file and counts the occurrences
of each User-Agent in the log entries.

Usage:
    python script.py <access_log_file>
"""

import sys
import re
from collections import Counter

# Regular expression pattern for Apache Combined Log Format
log_pattern = re.compile(r'''
    (?P<ip>\S+)                    # IP address
    \s+
    (?P<identd>\S+)                # identd
    \s+
    (?P<user>\S+)                  # userid
    \s+
    \[(?P<date>.*?)\]              # date
    \s+
    "(?P<request>.*?)"             # request
    \s+
    (?P<status>\d{3})              # status code
    \s+
    (?P<size>\S+)                  # size
    \s+
    "(?P<referer>.*?)"             # referer
    \s+
    "(?P<user_agent>.*?)"          # user agent
    ''', re.VERBOSE)

def parse_access_log(file_path):
    """
    Parses an Apache access log file and counts User-Agent occurrences.

    Args:
        file_path (str): The path to the log file.

    Returns:
        Counter: A Counter object with User-Agent strings as keys and their
        counts as values.
    """
    user_agents = []
    try:
        with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
            for line in file:
                match = log_pattern.match(line)
                if match:
                    user_agents.append(match.group('user_agent'))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    return Counter(user_agents)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <access_log_file>")
        sys.exit(1)

    log_file_path = sys.argv[1]
    user_agent_counts = parse_access_log(log_file_path)

    print(f"Total number of different User Agents: {len(user_agent_counts)}")
    print("Number of requests from each User Agent:")
    for agent, count in user_agent_counts.items():
        print(f"{agent}: {count}")

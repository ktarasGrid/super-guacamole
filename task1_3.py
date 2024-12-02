'''

    Task 1

    1. Create a script that accepts the file name and puts its extension to output. If there is no extension - an exception should be raised.
    2. Given a list of integers. Remove duplicates from the list and create a tuple. Find the minimum and maximum number.
    3. Create a script that reads the access log from a file. The name of the file is provided as an argument. 
    An output of the script should provide the total number of different User Agents and then provide statistics with the number of requests from each of them.
    Here is a link to an example access.log file.
    4. Given an input string, count occurrences of all characters within a string (e.g. pythonnohtyppy -> p:3, y:3, t:2, h:2, o:2, n:2).
    5. Write a script that gets system information like distro info, memory(total, used, free), CPU info (model, core numbers, speed), 
    current user, system load average, and IP address. Use arguments for specifying resources. 
    (For example, -d for distro -m for memory, -c for CPU, -u for user info, -l for load average, -i for IP address).

'''

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

def parse_access_log(log_file):
    user_agents = []
    with open(log_file, 'r', encoding='utf-8', errors='replace') as file:
        for line in file:
            match = log_pattern.match(line)
            if match:
                user_agent = match.group('user_agent')
                user_agents.append(user_agent)
            else:
                pass
    return Counter(user_agents)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <access_log_file>")
        sys.exit(1)

    log_file = sys.argv[1]
    user_agent_counts = parse_access_log(log_file)

    print(f"Total number of different User Agents: {len(user_agent_counts)}")
    print("Number of requests from each User Agent:")
    for agent, count in user_agent_counts.items():
        print(f"{agent}: {count}")

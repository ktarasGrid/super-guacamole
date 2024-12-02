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

import argparse
import platform
import psutil
import os
import socket
import getpass

def get_distro_info():
    print(f"Distro Info: {platform.platform()}")

def get_memory_info():
    mem = psutil.virtual_memory()
    print(f"Memory Total: {mem.total / (1024 ** 3):.2f} GB")
    print(f"Memory Used: {mem.used / (1024 ** 3):.2f} GB")
    print(f"Memory Free: {mem.available / (1024 ** 3):.2f} GB")

def get_cpu_info():
    cpu_freq = psutil.cpu_freq()
    print(f"CPU Model: {platform.processor()}")
    print(f"CPU Cores: {psutil.cpu_count(logical=False)}")
    print(f"CPU Speed: {cpu_freq.current / 1000:.2f} GHz")

def get_user_info():
    print(f"Current User: {getpass.getuser()}")

def get_load_average():
    load1, load5, load15 = os.getloadavg()
    print(f"System Load Average (1 min): {load1}")
    print(f"System Load Average (5 min): {load5}")
    print(f"System Load Average (15 min): {load15}")

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"IP Address: {ip_address}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="System Information Script")
    parser.add_argument("-d", action="store_true", help="Show distro info")
    parser.add_argument("-m", action="store_true", help="Show memory info")
    parser.add_argument("-c", action="store_true", help="Show CPU info")
    parser.add_argument("-u", action="store_true", help="Show user info")
    parser.add_argument("-l", action="store_true", help="Show load average")
    parser.add_argument("-i", action="store_true", help="Show IP address")
    
    args = parser.parse_args()

    if args.d:
        get_distro_info()
    if args.m:
        get_memory_info()
    if args.c:
        get_cpu_info()
    if args.u:
        get_user_info()
    if args.l:
        get_load_average()
    if args.i:
        get_ip_address()

    if not any(vars(args).values()):
        parser.print_help()

"""
This script provides various system information such as distribution details,
memory usage, CPU info, current user, load averages, and IP address.

Usage:
    python task1_5.py [-d] [-m] [-c] [-u] [-l] [-i]

Options:
    -d    Show distribution information
    -m    Show memory information
    -c    Show CPU information
    -u    Show current user information
    -l    Show system load average
    -i    Show IP address
"""

import os
import argparse
import socket
import getpass
import platform
import psutil


def get_distro_info():
    """Prints the distribution information of the operating system."""
    print(f"Distro Info: {platform.platform()}")


def get_memory_info():
    """Prints the memory usage information."""
    mem = psutil.virtual_memory()
    print(f"Memory Total: {mem.total / (1024 ** 3):.2f} GB")
    print(f"Memory Used: {mem.used / (1024 ** 3):.2f} GB")
    print(f"Memory Free: {mem.available / (1024 ** 3):.2f} GB")


def get_cpu_info():
    """Prints the CPU details, including model, cores, and speed."""
    cpu_freq = psutil.cpu_freq()
    print(f"CPU Model: {platform.processor()}")
    print(f"CPU Cores: {psutil.cpu_count(logical=False)}")
    print(f"CPU Speed: {cpu_freq.current / 1000:.2f} GHz")


def get_user_info():
    """Prints the current username."""
    print(f"Current User: {getpass.getuser()}")


def get_load_average():
    """Prints the system load average for the last 1, 5, and 15 minutes."""
    load1, load5, load15 = os.getloadavg()
    print(f"System Load Average (1 min): {load1}")
    print(f"System Load Average (5 min): {load5}")
    print(f"System Load Average (15 min): {load15}")


def get_ip_address():
    """Prints the IP address of the current machine."""
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"IP Address: {ip_address}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="System Information Script")
    parser.add_argument("-d", action="store_true", help="Show distribution info")
    parser.add_argument("-m", action="store_true", help="Show memory info")
    parser.add_argument("-c", action="store_true", help="Show CPU info")
    parser.add_argument("-u", action="store_true", help="Show user info")
    parser.add_argument("-l", action="store_true", help="Show system load average")
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

    # Print help if no arguments are provided
    if not any(vars(args).values()):
        parser.print_help()

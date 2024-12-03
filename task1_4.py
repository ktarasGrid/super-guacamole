"""
This script counts the frequency of each character in a user-provided string
and displays the results.

Usage:
    python task1_4.py
"""

from collections import Counter

def count_characters(input_string):
    """
    Counts the frequency of each character in the given string.

    Args:
        input_string (str): The string to analyze.

    Returns:
        Counter: A Counter object with characters as keys and their counts as values.
    """
    return Counter(input_string)

if __name__ == "__main__":
    input_str = input("Enter a string: ")
    char_counts = count_characters(input_str)

    for char, count in char_counts.items():
        print(f"{char}: {count}")

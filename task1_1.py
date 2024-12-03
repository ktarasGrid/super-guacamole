"""
This script retrieves the file extension from a given filename.
Usage: python task1_1.py <filename>
"""

import sys
import os

def get_file_extension(file_path):
    """
    Extracts and returns the file extension from a given file path.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The file extension (including the dot).

    Raises:
        ValueError: If the file has no extension.
    """
    _, extension = os.path.splitext(file_path)
    if not extension:
        raise ValueError("No extension found in the filename.")
    return extension

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python task1_1.py <filename>")
        sys.exit(1)

    try:
        input_filename = sys.argv[1]
        file_extension = get_file_extension(input_filename)
        print(f"The extension is: {file_extension}")
    except ValueError as error:
        print(error)

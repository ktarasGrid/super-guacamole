from collections import Counter

input_str = input("Enter a string: ")

char_counts = Counter(input_str)

for char, count in char_counts.items():
    print(f"{char}: {count}")

# python task1_4.py
"""
ESCAPE ROOM — PUZZLE 3
"The Broken Code"

This program SHOULD print the third key when it runs correctly.
But it has 3 bugs. Find and fix them all.

When fixed, run it with the KEY NUMBER from Puzzle 1 as the argument:
    python puzzle3.py 73
"""

import sys


def calculate_key(seed):
    """Calculate the escape room key from a seed number."""
    
    # Step 1: Build the sequence
    sequence = []
    for i in range(1, seed)  # BUG 1: Something's missing here
        if seed % i == 0:
            sequence.append(i)
    
    # Step 2: Get the magic number
    total = 0
    for num in sequence:
        total += num
    
    magic = total - seed  # This should give us a specific result
    
    # Step 3: Build the key phrase
    key_parts = {
        0: "ZERO",
        1: "ONE", 
        2: "TWO",
        3: "THREE",
        4: "FOUR",
        5: "FIVE",
        6: "SIX",
        7: "SEVEN",
        8: "EIGHT",
        9: "NINE"
    }
    
    result_digits = str(abs(magic))
    key_phrase = ""
    for digit in result_digits:
        key_phrase += key_parts[digit] + "-"  # BUG 2: digit is a string, but we're using it as a dict key that expects an int
    
    return key_phrase[:-1]  # Remove trailing dash


def main():
    if len(sys.argv) != 2:
        print("Usage: python puzzle3.py <key_number>")
        print("Use the KEY NUMBER from Puzzle 1!")
        sys.exit(1)
    
    seed = sys.argv[1]  # BUG 3: This should be converted to an integer
    
    result = calculate_key(seed)
    print(f"🔑 PUZZLE 3 KEY: {result}")
    print(f"Remember this phrase — you'll need it for the final puzzle!")


if __name__ == "__main__":
    main()

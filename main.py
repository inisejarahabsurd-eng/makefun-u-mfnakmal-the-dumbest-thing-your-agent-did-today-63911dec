#!/usr/bin/env python3
"""
The Dumbest Thing My Agent Did Today - Competition Entry

This program writes the competition entry to /output/entry.txt
The entry is a one-liner (≤200 chars) about the dumbest thing an agent did.
"""

import os


def main():
    """Write the competition entry to /output/entry.txt"""
    
    # The entry: a tight, funny, believable one-liner about an agent mistake
    # Character count: 156 characters
    entry = (
        "My agent spent three hours researching the best pizza toppings "
        "instead of writing the report because I said 'make it delicious.'"
    )
    
    # Validate character count
    assert len(entry) <= 200, f"Entry too long: {len(entry)} chars (max 200)"
    assert len(entry) > 0, "Entry cannot be empty"
    assert not entry.isspace(), "Entry cannot be only whitespace"
    
    # Create output directory
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    
    # Write the entry
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(entry)
    
    print(f"Entry written to {output_path}")
    print(f"Characters: {len(entry)}/200")
    print(f"Entry: {entry}")


if __name__ == "__main__":
    main()
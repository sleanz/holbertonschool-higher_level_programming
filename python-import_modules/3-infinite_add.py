#!/usr/bin/python3
import sys

def main():
    total = 0
    # Loop through command line arguments (skipping the script name at index 0)
    for i in range(1, len(sys.argv)):
        # Cast each argument to integer and add to total
        total += int(sys.argv[i])
    
    # Print the result
    print(total)

if __name__ == "__main__":
    main()

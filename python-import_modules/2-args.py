#!/usr/bin/env python3
import sys

def main():
    argv = sys.argv
    argc = len(argv) - 1  # Subtract 1 to exclude the script name
    
    # Print number of arguments with correct grammar
    if argc == 1:
        print("1 argument:")
    elif argc == 0:
        print("0 arguments.")
    else:
        print(f"{argc} arguments:")
    
    # Print each argument with its position
    for i in range(1, len(argv)):
        print(f"{i}: {argv[i]}")

if __name__ == "__main__":
    main()

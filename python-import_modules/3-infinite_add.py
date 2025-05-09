#!/usr/bin/env python3
import sys

def print_arguments():
    argv = sys.argv[1:]  # Skip the first argument (script name)
    argc = len(argv)
    
    # Print the number of arguments with proper grammar
    if argc == 1:
        print("1 argument:")
    elif argc == 0:
        print("0 arguments.")
    else:
        print(f"{argc} arguments:")
    
    # Print each argument with its position
    for i in range(argc):
        print(f"{i+1}: {argv[i]}")

if __name__ == "__main__":
    print_arguments()

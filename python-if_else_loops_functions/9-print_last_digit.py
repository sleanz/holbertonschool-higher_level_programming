#!/usr/bin/python3
def print_last_digit(number):
    """
    Function that prints the last digit of a number
    Returns the value of the last digit
    """
    last_digit = abs(number) % 10
    print("{}".format(last_digit), end="")
    return last_digit
#!/usr/bin/python3
def fizzbuzz():
    """
    Function that prints numbers from 1 to 100
    For multiples of 3, prints Fizz
    For multiples of 5, prints Buzz
    For multiples of both 3 and 5, prints FizzBuzz
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
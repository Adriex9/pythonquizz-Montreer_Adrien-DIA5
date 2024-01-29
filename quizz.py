# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 17:18:01 2024

@author: Ariex
"""

import random

def quizz():
    i = random.randint(0,3)

    if i == 0:
        print("What is 2 + 2?")
        print("a: 3 \nb: 5 \nc: 8 \nd: 4")
        k = input("Your answer (a, b, c, d): ").lower()
        while k != "d":
            if k not in ["a", "b", "c", "d"]:
                print("Please answer with a, b, c, or d.")
            else:
                print("That's not the correct answer.")
            k = input("Try again: ").lower()
        print(f"Indeed, {k} is the correct answer.")
        
    elif i == 1:
        print("What is 2 - 2?")
        print("a: 0 \nb: 6 \nc: 9 \nd: 10")
        k = input("Your answer (a, b, c, d): ").lower()
        while k != "a":
            if k not in ["a", "b", "c", "d"]:
                print("Please answer with a, b, c, or d.")
            else:
                print("That's not the correct answer.")
            k = input("Try again: ").lower()
        print(f"Indeed, {k} is the correct answer.")

    elif i == 2:
        print("What is 2 * 2?")
        print("a: 1 \nb: 6 \nc: 4 \nd: 9")
        k = input("Your answer (a, b, c, d): ").lower()
        while k != "c":
            if k not in ["a", "b", "c", "d"]:
                print("Please answer with a, b, c, or d.")
            else:
                print("That's not the correct answer.")
            k = input("Try again: ").lower()
        print(f"Indeed, {k} is the correct answer.")

    elif i == 3:
        print("What is 2 / 2?")
        print("a: -5 \nb: 1 \nc: 9 \nd: 15")
        k = input("Your answer (a, b, c, d): ").lower()
        while k != "b":
            if k not in ["a", "b", "c", "d"]:
                print("Please answer with a, b, c, or d.")
            else:
                print("That's not the correct answer.")
            k = input("Try again: ").lower()
        print(f"Indeed, {k} is the correct answer.")

    return None

# Running the quiz function
if __name__ == "__main__":
    quizz()

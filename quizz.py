# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 17:18:01 2024

@author: Ariex
"""

import random

def quiz():
    questions = [
        {
            "question": "What is 2+2?",
            "options": ["a", "b", "c", "d"],
            "correct": "d",
            "answers": lambda: [random.randint(0, 2), random.randint(5, 7), random.randint(8, 9), 4]
        },
        {
            "question": "What is 2-2?",
            "options": ["a", "b", "c", "d"],
            "correct": "a",
            "answers": lambda: [0, random.randint(5, 7), random.randint(8, 9), random.randint(10, 100)]
        },
        {
            "question": "What is 2*2?",
            "options": ["a", "b", "c", "d"],
            "correct": "c",
            "answers": lambda: [random.randint(0, 2), random.randint(5, 7), 4, random.randint(8, 9)]
        },
        {
            "question": "What is 2/2?",
            "options": ["a", "b", "c", "d"],
            "correct": "b",
            "answers": lambda: [random.randint(-10, 0), 1, random.randint(8, 9), random.randint(10, 100)]
        }
    ]

    i = random.randint(0, len(questions) - 1)
    question = questions[i]

    print(question["question"])
    answers = question["answers"]()
    for idx, option in enumerate(question["options"]):
        print(f" {option}: {answers[idx]}")
    k = input("Please answer with the letter a, b, c, or d: ").lower()
    while k != question["correct"]:
        if k not in question["options"]:
            print("You must answer with the letter a, b, c, or d!")
        else:
            print("That's not the correct answer.")
        k = input("Please answer with the letter a, b, c, or d: ").lower()
    print(f"Indeed, {k} is the correct answer.")

if __name__ == "__main__":
    quiz()
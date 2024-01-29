# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 17:18:01 2024

@author: Ariex
"""

import random

def quizz():
    i = random.randint(0,3)
        
    if i ==0:
        print("what is 2+2 ")
        print(f" a: {random.randint(0,2)} \n b: {random.randint(5,7)} \n c: {random.randint(8,9)} \n d: 4")
        k=input()
        while k!="d":
            if k not in ["a","b","c","d"]:
                print("tu dois répondes avec la lettre a b c ou d !")
            else: 
                print("ce n'est pas la bonne réponses")
            k=input()
        print(f"en effet {k} est la bonne réponse ")
        return(None)
        
    if i ==1:
        print("what is 2-2 ")
        print(f" a: 0 \n b: {random.randint(5,7)} \n c: {random.randint(8,9)} \n d: {random.randint(10,100)}")
        k=input()
        while k!="a":
            if k not in ["a","b","c","d"]:
                print("tu dois répondes avec la lettre a b c ou d !")
            else: 
                print("ce n'est pas la bonne réponses")
            k=input()
        print(f"en effet {k} est la bonne réponse ")
        return(None)
    if i ==2:
        print("what is 2*2 ")
        print(f" a: {random.randint(0,2)} \n b: {random.randint(5,7)} \n c: 4 \n d: {random.randint(8,9)}")
        k=input()
        while k!="c":
            if k not in ["a","b","c","d"]:
                print("tu dois répondes avec la lettre a b c ou d !")
            else: 
                print("ce n'est pas la bonne réponses")
            k=input()
        print(f"en effet {k} est la bonne réponse ")
        return(None)
    if i ==3:
        print("what is 2/2 ")
        print(f" a: {random.randint(-10,0)} \n b: 1 \n c: {random.randint(8,9)} \n d: {random.randint(10,100)} ")
        k=input()
        while k!="b":
            if k not in ["a","b","c","d"]:
                print("tu dois répondes avec la lettre a b c ou d !")
            else: 
                print("ce n'est pas la bonne réponses")
            k=input()
        print(f"en effet {k} est la bonne réponse ")
        return(None)

    
    
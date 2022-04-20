''' EightPuzzleWithHamming.py
name: Romil Kinger
email: romilk@uw.edu
student id: 1837820
date: 19-oct-2019
CSE 415 Au19
Assignment 3
This file made from the scratch
'''
import math
from EightPuzzle import *

def h(self):
    C = 0
    #goal = GOAL_STATE
    for i in range(1,9):
        index = self.b[i//3][i%3]
        print (index)
        if index !=i:
            C += 1
    return C

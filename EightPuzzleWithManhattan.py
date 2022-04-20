''' EightPuzzleWithManhattan.py
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
    dist = 0
    for i in range(0,9):
        index = self.b[(i)//3][(i)%3]
        if(index !=0):
            (vi, vj) = (index // 3, index % 3)
            (wi, wj) = (i // 3, i % 3)
            dist += abs(vi - wi) + abs(vj - wj)
    return dist
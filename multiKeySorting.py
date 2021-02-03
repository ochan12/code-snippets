#!/bin/python3

import math
import os
import random
import re
import sys

class reversor:
    def __init__(self, obj):
        self.obj = obj

    def __eq__(self, other):
        return other.obj == self.obj

    def __lt__(self, other):
        return other.obj < self.obj


if __name__ == '__main__':
    s = input()
    letters = dict()
    for char in list(s):
        if(char in letters):
            letters[char]+=1
        else:
            letters[char]=1
    sorted_letters = sorted(letters.items(), key=lambda item: (item[1], reversor(item[0])), reverse=True)
    for i in range(3):
        print(str(sorted_letters[i][0])+ " " +str(sorted_letters[i][1]))

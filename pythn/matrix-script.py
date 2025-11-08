#!/bin/python3

import math
import os
import random
import re
import sys

# blorbo found "hard" pythen problem. thankfullly blorbo lives in the 6th dimension. 
# blorbo will try

first_multiple_input = input().rstrip().split()

N, M = [int(number) for number in first_multiple_input]


matrix = []
for _ in range(N):
    matrix_item = input()
    matrix.append(matrix_item)

msg = ''
for i in range(M): 
    for j in range(N): msg += matrix[j][i]

# print(msg)

new_msg = ''
trailing_head, trailing_tail = '', ''
head_alnum, tail_alnum = False, False  # bool switches
for char in msg:
    if char.isalnum():
        new_msg += char
        head_alnum, tail_alnum = True, True
    else:
        if tail_alnum:      # if switch was on, full reset
            trailing_tail = ''
            tail_alnum = False
        new_msg += " "
        if not head_alnum: trailing_head += char
        if not tail_alnum: trailing_tail += char

# print(trailing_tail)

new_msg = new_msg.split()
print("".join(trailing_head)+" ".join(new_msg)+"".join(trailing_tail))

'''
python3 matrix-script.py < inputs/matrix-script.txt | cat
'''
#!/usr/bin/env python3

import numpy as np

f = open("data/day2.txt", "r")
lists = []
for line in f.read().splitlines():
    lists.append(np.array(line.split(' '),dtype=int))



nSafe = 0
nSafe_dampened = 0

def isListSafe(alist):


    isSafe = 1

    d = np.diff(alist)
    if np.any(d==0): isSafe = 0
    if np.any(np.abs(d) > 3): isSafe = 0
    if np.any(d > 0) & np.any(d < 0) : isSafe = 0

    return(isSafe)



for a in lists:
    isSafeReturn = isListSafe(a)
    nSafe += isSafeReturn
    

for a in lists:
    isSafeReturn = isListSafe(a)
    nSafe_dampened += isSafeReturn

    if isSafeReturn == 0:
        for n in range(0,len(a)):
            remove = np.ones_like(a,dtype=bool)
            remove[n] = False
            if isListSafe(a[remove]) > 0:
                nSafe_dampened += 1
                break



print('number of safe lists =', nSafe)
print('number of dampened safe lists =', nSafe_dampened)


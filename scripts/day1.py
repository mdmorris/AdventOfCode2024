#!/usr/bin/env python3

import numpy as np

f = open("data/day1.txt", "r")
list1 = []
list2 = []
for line in f.read().splitlines():
    line_split = line.split('   ')
    list1.append(int(line_split[0]))
    list2.append(int(line_split[1]))

list1_sorted = np.sort(list1)
list2_sorted = np.sort(list2)


distance = np.abs(list2_sorted - list1_sorted)


print('sum of distances between sorted numbers =', np.sum(distance))
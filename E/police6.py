#!/usr/bin/env python3

from collections import Counter

N, M, L = map(int, input().strip().split())
D = [int(x) for x in input().strip().split()]

cur = 0  # counting the number of intervals at position 0
diff = Counter()  # how much the number of intervals changes at positions. Counter is a dictionary with default 0.
for d in D:
    dl, dr = d - M, d + M  # left and right borders of the interval
    if dl <= 0:
        cur += 1  # this interval is active at position 0
    else:
        diff[dl] += 1  # left border of the interval
    if dr < L:
        diff[dr] -= 1  # right border of the interval
best = cur
for _, delta in sorted(diff.items()):  # sort by position and look at variations in numbers of intervals
    cur += delta
    if cur < best:
        best = cur
print(best)
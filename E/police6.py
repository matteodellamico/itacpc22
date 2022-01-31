#!/usr/bin/env python3

from collections import Counter

N, M, L = map(int, input().strip().split())
D = [int(x) for x in input().strip().split()]

cur = 0
diff = Counter()
for d in D:
    dl, dr = d - M, d + M
    if dl <= 0:
        cur += 1
    else:
        diff[dl] += 1
    if dr < L:
        diff[dr] -= 1
best = cur
for _, delta in sorted(diff.items()):
    cur += delta
    if cur < best:
        best = cur
print(cur)
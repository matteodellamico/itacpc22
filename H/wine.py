#!/usr/bin/env python3

from heapq import heapify, heappop, heapreplace

n, k = map(int, input().strip().split())
v = list(map(int, input().strip().split()))

q = [(v, i, i + 1) for i, v in enumerate(v)]
heapify(q)

for _ in range(k):
    s, l, r = q[0]
    try:
        s += v[r]
    except IndexError:
        heappop(q)
    else:
        heapreplace(q, (s, l, r + 1))
print(l, r - 1)
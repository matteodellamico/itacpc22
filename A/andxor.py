#!/usr/bin/env python3

def print_solution(state):
    n, xor = max(state)
    print(n - (not bool(xor)))


# input data
_, n_queries = map(int, input().strip().split())
values = list(map(int, input().strip().split()))

masks = [1 << i for i in range(20)]

state = []
for m in masks:
    n, xor = 0, 0
    for v in values:
        if m & v:
            n += 1
            xor ^= v
    state.append((n, xor))

print_solution(state)

for _ in range(n_queries):
    pos, new = map(int, input().strip().split())
    pos -= 1  # 1-based indexing is BAD
    old = values[pos]
    values[pos] = new
    for i, ((n, xor), m) in enumerate(zip(state, masks)):
        if m & old:
            n -= 1
            xor ^= old
        if m & new:
            n += 1
            xor ^= new
        state[i] = n, xor
    print_solution(state)

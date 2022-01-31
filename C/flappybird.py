#!/usr/bin/env python3

def parse_line():
    return map(int, input().strip().split())

N = int(input().strip())
old_a, old_b = parse_line()
for _ in range(N - 1):
    new_a, new_b = parse_line()
    if max(new_a, old_a) > min(new_b, old_b):
        print("NO")
        break
    old_a, old_b = new_a, new_b
else:  # no break
    print("YES")

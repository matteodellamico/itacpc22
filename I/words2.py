#!/usr/bin/env python3

W = input().strip()
m = 1_000_000_007
ord_a = ord('a')
p = 1
n = 0
for c in W[::-1]:  # inverted
    n = (n + (ord(c) - ord_a) * p) % m
    p = (p * 26) % m
    n = (n + p) % m
n = (n - p) % m  # ask for forgiveness rather than permission
print(n)
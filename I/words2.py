#!/usr/bin/env python3

W = input().strip()
m = 1_000_000_007
ord_a = ord('a')
p = 1  # base
n = 0  # solution
for c in reversed(W):
    n = (n + (ord(c) - ord_a) * p) % m
    p = (p * 26) % m  # increase the base
    n = (n + p) % m  # add all to the result all the words of length i
n = (n - p) % m  # reverse the last operation for the last character
print(n)
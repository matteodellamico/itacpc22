#!/usr/bin/env python3

rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
table = str.maketrans(''.join(row[:-1] for row in rows),
                      ''.join(row[1:] for row in rows))

input()  # N, not needed
S = input().strip()
print(S.translate(table))  # print the result

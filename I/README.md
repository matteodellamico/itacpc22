[Words, Just Words (I)](https://judge.itacpc.it/team/problems/15/text)
======================================================================

This problem is about seeing words essentially as base-26 numbers.

There are two tricks though.
The first depends on modulo arithmetic: you need to take the modulo after each operation
(the properties of modulo operations guarantee that we can do that without problems).
The second is that we need to take into account all the shorter words first: that's what's done with the
`n = (n + p) % m` line.
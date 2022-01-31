[The Sieve of Eratosthenes (G)](https://judge.itacpc.it/team/problems/17/text)
==============================================================================

Here we start with a list of numbers.
We want to remove all the numbers from the list with the least moves.
With each move we remove a number, its multiples and its divisors.
The problem is about finding the minimum number of moves to do it.

One, unfortunately not very helpful, way of seeing this problem is by seeing it as a
[set cover problem](https://en.wikipedia.org/wiki/Set_cover_problem): each move represents a set, and we want to find
out the least number of sets that can cover all the original list of numbers.
Unfortunately, set cover is NP-complete, so there are no efficient solutions to this problem.
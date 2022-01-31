[Police Investigation 6](https://judge.itacpc.it/team/problems/11/text)
=======================================================================

Here, we have overlapping intervals and we want to find, in a given segment, the minimum number of overlapping ones.

This is pretty much the same problem that is solved by
[Marzullo's algorithm](https://en.wikipedia.org/wiki/Marzullo%27s_algorithm)
(the algorithm looks for the maximum number of overlapping intervals, here we look for the minimum but the logic stays
the same).
I implemented it using Python's
[collections.Counter](https://docs.python.org/3/library/collections.html#collections.Counter) to easily aggregate all
changes of intervals happening in the same place.
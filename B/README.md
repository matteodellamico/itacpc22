[Training for the Marathon (B)](https://judge.itacpc.it/team/problems/16/text)
==============================================================================

Here the core of the problem is computing efficiently the connected components of a graph.
Given the size of the problem, we need a subquadratic solution.

Something we can notice is that we start with a connected graph having N nodes and N-1 edges.
This means we necessarily have a tree (not enough edges to connect everything and have loops).
In turn this means that removing an edge disconnects something.

I think this can be solved efficiently with a dynamic algorithm for spanning trees such as the one described in https://resources.mpi-inf.mpg.de/departments/d1/teaching/ss12/AdvancedGraphAlgorithms/Slides08.pdf.
However all of it is quite difficult to implement (one would need to implement Euler tours and balanced trees).
I wonder whether there's a simpler solution that can be implemented.
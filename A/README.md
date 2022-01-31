[A: Bitwise Party](https://judge.itacpc.it/team/problems/9/text)
================================================================

Here we have N integers and we have to find out the largest number of them that have at once nonzero bitwise AND and XOR.

Moreover, we'll have updates: the i-th element will be swapped, and we'll have to update the solution.

N can be up to 200,000 and we have a time limit of 1.5 s, so we need a subquadratic solution. Values are less than 2^20.  

My solution is based on considering that:
 * to have nonzero AND, all elements of a group have to have a 1 bit in common
 * if a group of x elements has zero XOR, just removing one of them makes the XOR nonzero

Based on this, the solution is quite straightforward:
 * create 19 1-bit masks 2^1, 2^2, ..., 2^19
 * for each mask `m`, keep the count and aggregate XOR of input values that match the mask (i.e., nonzero `x & m`)

The solution is obtained by finding the largest count (breaking ties with XOR), and subtracting 1 if XOR is zero.

Updates are simple:
 * to remove a value `v_old`, we subtract 1 and XOR `v_old` for all matching masks
 * to insert a value `v_new`, we add 1 and XOR `v_new` for all matching masks
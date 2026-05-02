160

第 3 章：向量空間與子空間

reduction to U and back substitution for x is slightly faster. Now we prefer the complete reduction: a single “1” in each pivot column. Everything is so clear in R (and the computer should do the hard work anyway) that we reduce all the way.

**REVIEW OF THE KEY IDEAS**

1. The rank r is the number of pivots. The matrix R has m – r zero rows.
2. Ax = b is solvable if and only if the last m – r equations reduce to 0 = 0.
3. One particular solution x<sub>p</sub> has all free variables equal to zero.
4. The pivot variables are determined after the free variables are chosen.
5. Full column rank r = n means no free variables: one solution or none.
6. Full row rank r = m means one solution if m = n or infinitely many if m < n.

**WORKED EXAMPLES**

3.4 A This question connects elimination (pivot columns and back substitution) to column space-nullspace-rank-solvability (the full picture). A has rank 2:

Ax = b is
```
x₁ + 2x₂ + 3x₃ + 5x₄ = b₁
2x₁ + 4x₂ + 8x₃ + 12x₄ = b₂
3x₁ + 6x₂ + 7x₃ + 13x₄ = b₃
```

1. Reduce [A b] to [U c], so that Ax = b becomes a triangular system Ux = c.
2. Find the condition on b₁, b₂, b₃ for Ax = b to have a solution.
3. Describe the column space of A. Which plane in R³?
4. Describe the nullspace of A. Which special solutions in R⁴?
5. Find a particular solution to Ax = (0, 6, -6) and then the complete solution.
6. Reduce [U c] to [R d]: Special solutions from R, particular solution from d.

Solution

1. The multipliers in elimination are 2 and 3 and –1. They take [A b] into [U c].
```
[ 1  2  3  5 | b₁ ]   [ 1  2  3  5 | b₁ ]
[ 2  4  8 12 | b₂ ] → [ 0  0  2  2 | b₂ - 2b₁ ]
[ 3  6 7 13 | b₃ ]   [ 0  0 -2 -2 | b₃ - 3b₁ ]
```

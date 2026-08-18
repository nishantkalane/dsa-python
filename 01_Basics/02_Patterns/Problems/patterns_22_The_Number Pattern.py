"""
Problem: The Number Pattern
Given and integer N, print the following pattern
3 3 3 3 3
3 2 2 2 3
3 2 1 2 3
3 2 2 2 3
3 3 3 3 3
Here n=3

Platform:
Strivers sheet

Topic:
Getting the minimum distance

Difficulty:
Hard

Approach:
-We need to print a square matrix of size (2 * n - 1) × (2 * n - 1). The outermost border should contain n, the next inner layer n-1, then n-2, and so on until the center which contains 1. This creates a concentric square pattern.
(i.e for n input we need 2n-1 rows and columns in pattern)
(The whole idea is to get the input, then convert it into the actual input we need n
after which we print the matrix of minmum distance from the wall and minus it from the inp input we had
we get our desired patern)
We use two nested loops:
    Outer loop runs for rows (i from 0 to 2n-2).
    Inner loop runs for columns (j from 0 to 2n-2).
For each cell (i, j), compute its distance from all four borders:
    top = i
    left = (2n - 2) - i
    bottom = j
    right = (2n - 2) - j
Take the minimum of these four distances. This tells us how deep we are inside the square.
Print n - minDistance at that position.

Time Complexity:
-
O((2N-1)²) ≈ O(N²), since we print every cell once.
Space Complexity:
-
O(1), only variables for indices are used.
Date Solved:
-18-AUG-2026

Mistake:
- Coludn't get inside rows

Key Takeaway:
- To print the number pattern in decreasing way and in square perimeters,
we first increase input to right input and then print the matrix of minimum distance, and we will minus the minimum distance pattern from our main input

Revision:
[ ] Rev 1
[ ] Rev 2
[ ] Rev 3
"""


class Solution:

    def solve(self,inp,n):
            for i in range(n):
                for j in range(n):
                    print(inp-min(i,j,n-1-i,n-1-j),end=" ")
                print()

if __name__ == "__main__":
    solution = Solution()

    # Test your solution
    inp=4
    n=2*inp-1
    solution.solve(inp,n)

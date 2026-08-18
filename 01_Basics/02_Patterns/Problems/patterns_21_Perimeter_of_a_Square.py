"""
Problem: Hollow Rectangle Pattern
Given an integer N, print the following pattern:
* * * *
*     *
*     *
* * * *

Platform:
-Strivers

Topic:
-Printing hollowness

Difficulty:
hard

Approach:
- we need to print a square of size n*n but only eith stars on the border, leaving the
inner cells as spaces. This creates a "hollow square" effect.
    run an outer loop i from 0 to n-1
    Inside run the row of increasing triangle till range only i and not i+1 so that the pattern doesn't overlap
    Keep the second decreasing triangle running from i to n
    in bot inner loop for each position:
        if it lies on the border(i ==0, j==0, i==n-1, j==n-1)
         print *
        else, print a space
    after printing the row move to the next line.

    another way :
    since it a is a square you can go directly with n no need of triangles

Time Complexity:
- O(N^2)

Space Complexity:
-O(1)
Date Solved:
-18/08/2026

Mistake:
-My two loops overlapped at the shared boundary, printing one extra column per row (off-by-one error).

Key Takeaway:
- When splitting a row into two loops, make sure they cover the range exactly once—no gaps, no overlaps. Always trace a small case by hand to catch off-by-one errors.


Revision:
[ ] Rev 1
[ ] Rev 2
[ ] Rev 3
"""


class Solution:

    def solve(self,n):
        for i in range(n):
            for j in range(i):
                if(i==0 or j==0 or i ==n-1 or j== n-1):
                    print("*",end=" ")
                else:
                    print(" ", end=" ")
            for j in range(i,n):

                if (i==0 or j==0 or i ==n-1 or j== n-1):
                    print("*", end=" ")

                else:
                    print(" ",end=" ")
            print()

if __name__ == "__main__":
    solution = Solution()

    # Test your solution here
    n=4
    solution.solve(n)
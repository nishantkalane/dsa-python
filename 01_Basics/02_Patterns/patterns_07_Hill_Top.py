"""
Problem:
Given an integer N, print the following pattern:

    *
   ***
  *****
 *******
*********

Platform:
Striver's Sheet

Topic:
Pattern Printing

Pattern:
Pyramid / Hill Pattern

Difficulty:
Easy

Approach:
The pyramid is built using three parts:

1. Decreasing number of leading spaces.
2. Increasing number of stars.
3. Increasing number of stars.

The outer loop controls the rows.

The two star loops together produce the increasing
number of stars needed for the pyramid.

Time Complexity:
O(N²)

Space Complexity:
O(1)

Date Solved:
14/08/2026

Mistake:
Initially used i + 1 in the first star loop instead of i,
which added an extra column and prevented the hill top
from being formed correctly.

Key Takeaway:
Complex patterns can be built by combining simpler
patterns.

For a pyramid, the spacing must also be considered,
and the number of printed characters should remain
consistent across the inner loops.

Revision:
[ ] Rev 1
[ ] Rev 2
[ ] Rev 3
"""

class Solution():
    def pattern_07(self,n):
        for i in range(n):
            #Printing leading spaces of decreasing triangle
            for j in range(i,n):
                print(" ", end =" ")
            #Print Stars of increasing triangle 1
            #Keep the range to i instead of i+1 to remove one column and have a hill top
            for j in range(i):
                print("*", end=" ")
            #Print stars of decreasing triangle
            for j in range(i+1):
                print("*",end=" ")
            print()
if __name__ == "__main__":
    sol=Solution()
    n=5
    sol.pattern_07(n)



"""
Problem:
Given an integer N, print the following pattern:

*********
 *******
  *****
   ***
    *

Platform:
Striver's Sheet

Topic:
Pattern Printing

Pattern:
Inverted Pyramid / Reverse Hill

Difficulty:
Easy

Approach:
The pattern is the inverted version of the star pyramid.

1. Increase the number of leading spaces.
2. Decrease the number of stars in each row.
3. Use two star loops to form the decreasing star pattern.
4. Remove one column from the first star loop to form the
   correct hill shape.

Time Complexity:
O(N²)

Space Complexity:
O(1)

Date Solved:
12/08/2026

Mistake:
Initially used range(i, n) in the first star loop.
This printed one extra column and the hill shape was incorrect.
Changing it to range(i, n - 1) removed the extra column.

Key Takeaway:
When combining patterns, adjusting the range by one can
be necessary to avoid duplicating the middle/edge element.

Revision:
[ ] Rev 1
[ ] Rev 2
[ ] Rev 3
"""

class Solution:
    def pattern_08(self,n):
        for i in range(n):
            #Print left spaces
            for j in range(i+1):
                print(" ", end=" ")
            #Print decreasing triangle stars
            #Adjust the (i,n) to print the hill top
            for j in range(i,n-1):
                print("*", end=" ")
            #Print stars of leading decreasing triangle
            for j in range(i,n):
                print("*", end= " ")
            print()


if __name__ == "__main__":
    sol=Solution()
    n=5
    sol.pattern_08(n)

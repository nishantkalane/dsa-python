"""
Problem:
Given an integer N, print a diamond pattern of stars.

Example:
    *
   ***
  *****
 *******
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
Diamond Pattern

Difficulty:
Medium

Approach:
Build the diamond using two parts:

1. Erect pyramid
   - Increasing stars
   - Decreasing leading spaces

2. Inverted pyramid
   - Decreasing stars
   - Increasing leading spaces

The last row of the erect pyramid is omitted so that
the middle row is not printed twice.

Time Complexity:
O(N²)

Space Complexity:
O(1)

Date Solved:
12/08/2026

Mistake:
-

Key Takeaway:
Complex patterns can be created by combining previously
learned patterns.

When combining two patterns, check whether a row is
being duplicated at the joining point.

Revision:
[ ] Rev 1
[ ] Rev 2
[ ] Rev 3
"""

class Solution:
    def pattern_09(slef,n):
        # erect pyramid One row is deleted to keep the diamond shape
        for i in range(n-1):
            for j in range(i,n):
                print(" ", end =" ")
                        #Keep the range to i instead of i+1 to remove one colimn and have a hill top
            for j in range(i):
                print("*", end=" ")
            for j in range(i+1):
                print("*",end=" ")
            print()

        for i in range(n):
            for j in range(i+1):
                print(" ", end=" ")
            #Adjust the (i,n) to print the hill top
            for j in range(i,n-1):
                print("*", end=" ")
            for j in range(i,n):
                print("*", end= " ")
            print()


if __name__ == "__main__":
    sol=Solution()
    n=5
    sol.pattern_09(n)


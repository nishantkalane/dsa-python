"""
Problem:
Given an integer N, print the following pattern:

*
**
***
****
*****
****
***
**
*

Platform:
Striver's Sheet

Topic:
Pattern Printing

Pattern:
Half Diamond

Difficulty:
Easy

Approach:
Build the pattern using two parts:

1. Increasing triangle
2. Decreasing triangle

The last row of the increasing triangle is omitted so
that the middle row is not printed twice.

Time Complexity:
O(N²)

Space Complexity:
O(1)

Date Solved:
14/08/2026

Mistake:
Initially did not remove the middle row, which caused
the maximum row to be printed twice.

Key Takeaway:
When combining increasing and decreasing patterns,
remove the common middle row to avoid duplication.

Revision:
[ ] Rev 1
[ ] Rev 2
[ ] Rev 3
"""
class Solution():
    def pattern_10(self,n):
        # Increasing triangle — omit last row
        for i in range(n-1):
            for j in range(i+1):
                print("*", end=" ")
            print()
        #Decreasing triangle
        for i in range(n):
            for j in range(i,n):
                print("*", end=" ")
            print()

if __name__ == "__main__":
    sol=Solution()
    n=5
    sol.pattern_10(n)

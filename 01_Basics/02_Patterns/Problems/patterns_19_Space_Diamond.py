"""
Problem: diamond void pattern:
Given and integer N, print the following pattern:

**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
Here n =5

Topic:
Multi Star printing

Difficulty:
medium

Approach:
- We first analyze the pattern
- Then decide on how many triangle patterns and in what way
- Kepp the record of the spaces and the pattern is being followed by removing rows and columns
- addjust the middle two inner loops to remove the uneasy patterns
Time Complexity:
- O(N^2)

Space Complexity:
- O(1)

Date Solved:
- 17-Aug-2026

Key Takeaway:
- Check what is asked in question do we need space in end or not

Revision:
[ ] Rev 1
[ ] Rev 2
[ ] Rev 3
"""


class Solution:

    def solve(self,n):
        for i in range(n):
            for j in range(i,n):
                print("*",end="")
            for j in range(i):
                print(" ", end="")
            for j in range(i):
                print(" ", end="")
            for j in range(i, n):
                print("*", end="")
            print()
        for i in range(n):
            for j in range(i+1):
                print("*",end="")
            for j in range(i, n-1):
                print(" ", end="")
            for j in range(i, n-1):
                print(" ", end="")
            for j in range(i+1):
                print("*", end="")
            print()


if __name__ == "__main__":
    solution = Solution()

    # Test your solution here
    n=5
    solution.solve(n)










"""
Problem: Space_hour_glass_or_Butterfly

Given an integer n, print the following pattern
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *

Here n=5

Topic:
Printing patterns

Difficulty:
medium

Approach:
- This patterns prints two symmetrical right-angled triangles facing each other
with spaces in between.

    -Run two for loops one for upper part one for below part
    -in upper for loop print the pattern using increasing and decreasing pattern
    -decrease n-1 in outer for loop so not to print the last row and to have symmetry
    - run the inner 2 loops till n-1 so that extra space is not added
    -in lower for loop print the pattern using increasing and decreasing pattern
    - run the inner 2 loops till i so that extra space is not added


Time Complexity:
- O(N^2)

Space Complexity:
-O (1)

Date Solved:
- 17 Aug 2026


Key Takeaway:
- Adjust the pattern properly by decreasing the middle row from upper for loop

Revision:
[ ] Rev 1
[ ] Rev 2
[ ] Rev 3
"""


class Solution:

    def solve(self,n):
        #decreasing n to have a symmetry
        for i in range(n-1):
            for j in range(i+1):
                print("*", end="")
            for j in range(i,n-1):
                print(" ", end="")
            for j in range(i,n-1):
                print(" ", end="")
            for j in range(i+1):
                print("*", end="")
            print()
        for i in range(n):
            for j in range(i,n):
                print("*", end="")
            for j in range(i):
                print(" ", end="")
            for j in range(i):
                print(" ", end="")
            for j in range(i,n):
                print("*", end="")
            print()



if __name__ == "__main__":
    solution = Solution()

    # Test your solution here
    n=5
    solution.solve(n)
"""
Problem:
Platform:
Link:

Topic:
Pattern:
Difficulty:

Approach:
-

Time Complexity:
-

Space Complexity:
-

Date Solved:
-

Mistake:
-

Key Takeaway:
-

Revision:
[ ] Rev 1
[ ] Rev 2
[ ] Rev 3
"""


class Solution:

    def solve(self,inp,n):
        for i in range(n):
            for j in range(n):
                print(inp-min(i, n-1-i, j, n-1-j),end=" ")


            print()

if __name__ == "__main__":
    solution = Solution()

    # Test your solution here
    inp=int(input("Enter n:"))
    inter = inp-1
    n=inp +inter
    solution.solve(inp,n)
"""
Problem:
Given an integer N, print the following pattern:

1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

Platform:
Striver's Sheet

Topic:
Pattern Printing

Pattern:
Decreasing Number Pattern

Difficulty:
Medium

Approach:
The outer loop controls the rows.
For row i, the inner loop runs from i to n, so the
number of elements decreases with each row.

Initialize p = 1 inside the outer loop so that every
row starts from 1.
Increment p inside the inner loop so the numbers
increase across each row.

Time Complexity:
O(N²)

Space Complexity:
O(1)

Date Solved:
14/08/2026

Mistake:
-

Key Takeaway:
When a value needs to reset at the beginning of every
row, initialize it inside the outer loop.
When the value needs to increase across a row,
increment it inside the inner loop.

Revision:
[ ] Rev 1
[ ] Rev 2
[ ] Rev 3
"""

class Solution():
    def pattern_06(self,n):
        for i in range(n):
            #Initalize p=1 keeping it here resets it at the start of every row
            p = 1
            #Print numbers from p=1 to p=n
            for j in range(i,n):
                print(p, end=" ")
                #P is incremented here so that to have the increasing column numbers
                p +=1
            print()

if __name__ == "__main__":
    sol=Solution()
    n=5
    sol.pattern_06(n)

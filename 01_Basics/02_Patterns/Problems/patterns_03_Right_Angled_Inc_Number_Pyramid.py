"""
Problem:
Given an integer N, print the following pattern:

1
12
123
1234
12345

Platform:
Striver's Sheet

Topic:
Pattern Printing

Pattern:
Increasing Number Pattern

Difficulty:
Medium

Approach:
The outer loop controls the rows.
For each row, initialize p = 1 so the numbers restart from 1.
The inner loop runs i + 1 times.
Print p and increment it after every element.

Time Complexity:
O(N²)

Space Complexity:
O(1)

Date Solved:
12/08/2026

Mistake:
Initially kept p = 1 outside the outer loop.
This prevented p from resetting to 1 for every row.

Key Takeaway:
If a variable needs to restart for every row,
initialize it inside the outer loop.
If it needs to change after every element,
increment it inside the inner loop.

Revision:
[ ] Rev 1
[ ] Rev 2
[ ] Rev 3
"""
class Solution:

    def pattern_03(self,n):
        for i in range(n):
            #initialize p inside the for loop or it resets again and again to 1 to begin with 1 on each new line of row
            p = 1
            for j in range(i+1):
                print(p, end=" ")
                #increaminting p to print from 1 to i
                p +=1
            print()

if __name__ == "__main__":
    sol = Solution()
    n=5
    sol.pattern_03(n)


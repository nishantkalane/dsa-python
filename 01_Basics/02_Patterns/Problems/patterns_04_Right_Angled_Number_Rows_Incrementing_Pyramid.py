"""
Problem:
Given an integer N, print the following pattern:

1
22
333
4444
55555

Platform:
Striver's Sheet

Topic:
Pattern Printing

Pattern:
Increasing Number Pattern — Row Number Repeated

Difficulty:
Medium

Approach:
The outer loop controls the rows.
For row i, the inner loop runs i + 1 times.
The same number must be printed throughout a row,
so p is incremented only after the inner loop finishes.
p is initialized outside the outer loop so it persists
and increases from one row to the next.

Time Complexity:
O(N²)

Space Complexity:
O(1)

Date Solved:
13/08/2026

Mistake:
Did not keep the function name and function call consistent.
Initially used 1 directly inside the inner loop instead of p.

Key Takeaway:
Variable placement determines its behavior:
- Initialize outside outer loop → value persists between rows.
- Increment outside inner loop → value changes after each row.
- Keep the value unchanged inside inner loop → same number across the row.

Revision:
[ ] Rev 1
[ ] Rev 2
[ ] Rev 3
"""

class Solution:
    def pattern_04(self,n):
        #Initalize p outside the outer loop to keep it incrementing on start of every row
        p=1
        for i in range(n):
            for j in range(i+1):
                print(p, end=" ")
            #Incrementing the p to increase the count in next row
            p +=1
            print()

if __name__ == "__main__":
    sol = Solution()
    n=5
    sol.pattern_04(n)


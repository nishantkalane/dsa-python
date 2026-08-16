
"""
Problem:
Given an integer N, print a right-angled triangle pattern
where the number of stars increases by one in every row.

Example:
*
* *
* * *
* * * *
* * * * *

Platform:
Striver's Sheet

Topic:
Pattern Printing

Pattern:
Increasing Pattern

Difficulty:
Easy

Approach:
The outer loop controls the rows.
For row i, the inner loop runs i + 1 times to print
the required number of stars.
After each row, print() moves to the next line.

Time Complexity:
O(N²)  Outer loop runs N times , and the inner loop runs up to N stars overall

Space Complexity:
O(1)

Date Solved:
11/08/2026

Mistake:
Forgot the second == in:
if __name__ == "__main__":

Key Takeaway:
The number of elements can be made to increase with
the row number by using range(i + 1).

Revision:
[ ] Rev 1
[ ] Rev 2
[ ] Rev 3
"""

class Solution:
    def pattern_02(self,n):
        #Loop for rows
        for i in range(n):
            # i + 1 creates an increasing number of stars per row
            for j in range(i+1):
                #Print stars in each row
                print("*" ,end=" ")
            print()
if __name__ == "__main__" :
    sol= Solution()
    n=5
    sol.pattern_02(n)

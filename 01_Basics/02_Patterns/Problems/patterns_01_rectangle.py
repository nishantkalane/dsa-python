"""
Problem:
Given an integer N, print a square pattern of stars.

Example:
* * * *
* * * *
* * * *
* * * *

Platform:
Striver's Sheet

Topic:
Pattern Printing

Pattern:
Rectangle

Difficulty:
Easy

Approach:
The outer loop controls the rows.
The inner loop prints N stars in each row.
After each row, print() moves to the next line.

Time Complexity:
O(N²)

Space Complexity:
O(1)

Date Solved:
05/08/2026

Mistake:
-

Key Takeaway:
Outer loop → rows
Inner loop → columns/elements in each row

Revision:
[ ] Rev 1
[ ] Rev 2
[ ] Rev 3
"""


class Solution():
    def pattern1(self,n):
        for i in range(n):
            for j in range(n):
                print("*", end=' ')
            print()

sol=Solution()
n=int(input("How many stars do you want in your column and rows ? "))
sol.pattern1(n)



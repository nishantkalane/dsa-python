"""
Problem:
Given an integer N, print the following pattern:

* * * * *
* * * *
* * *
* *
*

Platform:
Striver's Sheet

Topic:
Pattern Printing

Pattern:
Decreasing Pattern — Inverted Right-Angled Triangle

Difficulty:
Easy

Approach:
The number of stars decreases by one in each row.
The outer loop controls the rows.
For row i, the inner loop runs from i to n,
giving n - i stars in that row.

Time Complexity:
O(N²)

Space Complexity:
O(1)

Date Solved:
14/08/2026

Mistake:
Used range(5) instead of range(n), which makes the
function work only for n = 5.

Key Takeaway:
For a decreasing pattern, the number of elements
decreases as the row number increases.

Revision:
[ ] Rev 1
[ ] Rev 2
[ ] Rev 3
"""

class Solution:
    def pattern_05(self,n):
        for i in range(5):
            #Number of stars decreases with each row
            for j in range(i,n):
                print("*" ,end=" ")
            print()
if __name__ ==  "__main__":
    sol=Solution()
    n=5
    sol.pattern_05(n)
'''
Observation: 
patterns_01_Decreasing_Right_angled_Triangle: 13/8/2026

Outer loop prints for rows n times from 0 to n-1
Inner loop prints for n times from 0 to n-1, we go from ( i to n) that (i,n)
Print was used inside the inner loop for printing the star and end=" "was added to keep the cursor on the same line
print() was used in outer loop to jump to next line as end= " " kept cursor on the same line.

'''
"""
Problem:
Problem Statement: Given an integer N, print the following pattern :

*
**
***
****
*****
Platform:
    Striver's sheet

Difficulty:
easy

Topic: Paterns
loops
rows
columns

Pattern:

Approach:


Time Complexity:

Space Complexity:

Date Solved:

Revision:
    □ Rev1
    □ Rev2
    □ Rev3

Notes:
"""

for i in range(5):
    for j in range(i+1):
        print("*" ,end=" ")
    print()

'''
Observation: 
patterns_01_rectangle: 5/8/2026

Outer loop prints for rows n times from 0 to n-1
Inner loop prints for n times from 0 to n-1
Print was used inside the inner loop for printing the star and end=" "was added to keep the cursor on the same line
print() was used in outer loop to jump to next line as end= " " kept cursor on the same line.

'''
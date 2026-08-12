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
def pattern_08_reverse_hill_top(n):
    for i in range(n):
        for j in range(i+1):
            print(" ", end=" ")
        for j in range(i,n-1):
            print("*", end=" ")
        for j in range(i,n):
            print("*", end= " ")
        print()

pattern_08_reverse_hill_top(5)



'''
Observation: 
patterns_01_rectangle: 5/8/2026

Outer loop prints for rows n times from 0 to n-1
Inner loop prints for n times from 0 to n-1
Print was used inside the inner loop for printing the star and end=" "was added to keep the cursor on the same line
print() was used in outer loop to jump to next line as end= " " kept cursor on the same line.


#mistake: Hill top didn't come had to remove one column by doing ( i, n-1) 
'''
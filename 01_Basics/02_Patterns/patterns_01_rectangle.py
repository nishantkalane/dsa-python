"""
Problem: Given an integer N, print the following pattern.
          * * * *
          * * * *
          * * * *
          * * * *

Platform:
    Striver's sheet

Difficulty: easy

Topic:
Nested Loops
rows
columns
printing on correct line

Approach:
Take an integer N as input to define the size of the square.
Use a loop from 0 to N-1 to represent each row.
Inside that loop, use another loop from 0 to N-1 to print stars in the current row.
Print "* " during each inner loop iteration to form the row.
After each inner loop completes, move to the next line.

Time Complexity: O(N^2)  As we print N stars for N times.

Space Complexity: O(1)

Date Solved:
5/8/2026

Revision:
    □ Rev1
    □ Rev2
    □ Rev3

Notes:

"""
class solution():
    def pattern1(self,n):
        for i in range(n):
            for j in range(n):
                print("*", end=' ')
            print()

sol=solution()
n=int(input("How many stars do you want in your column and rows ? "))
sol.pattern1(n)


'''
Observation: 
patterns_01_rectangle: 5/8/2026

Outer loop prints for rows n times from 0 to n-1
Inner loop prints for n times from 0 to n-1
Print was used inside the inner loop for printing the star and end=" "was added to keep the cursor on the same line
print() was used in outer loop to jump to next line as end= " " kept cursor on the same line.





'''
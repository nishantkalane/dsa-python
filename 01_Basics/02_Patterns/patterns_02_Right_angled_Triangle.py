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
printing

Approach:
This is one of the simplest star patterns. We need to form a right-angled triangle where the number of stars in each row increases line by line. Row i contains exactly i + 1 stars.
Run increasing pattern:
    Run an outer loop from 0 to N-1 to handle rows.
    For each row i, run an inner loop from 0 to i +1 for total N columns to print rightly.
    In the inner loop, print a star (*).
    After finishing the stars of one row, move to the next line using endl.

Time Complexity:
O(N^2), Outer loop runs N times , and the inner loop runs up to N stars overall
Space Complexity: O(1), No extra space is used apart from loop counters.
Date Solved:

Revision:
    □ Rev1
    □ Rev2
    □ Rev3

Notes:
"""
class Solution:
    #Function to pattern_02
    def pattern_02(self,n):
        #Loop for rows
        for i in range(n):
            #Loop for columns
            for j in range(i+1):
                #Print stars in each row
                print("*" ,end=" ")
            print()
if __name__ == "__main__" :
    #Create Solution object
    sol= Solution()
    #Define n
    n=5
    #Call pattern Function
    sol.pattern_02(n)

'''
Observation: 
patterns_01_rectangle: 11/8/2026

Outer loop prints for rows n times from 0 to n-1
Inner loop prints for n times from 0 to i+1
Print was used inside the inner loop for printing the star and end=" "was added to keep the cursor on the same line
print() was used in outer loop to jump to next line as end= " " kept cursor on the same line.

Using increasing pattern we can solve similar questions
mistakes: forgot to add 2 == after if __name__ ==

'''
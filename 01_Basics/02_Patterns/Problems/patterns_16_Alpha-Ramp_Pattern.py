"""
Problem: Alpha- Ramp Pattern
Given an integer N, print the following pattern:
 A
 B B
 C C C
 D D D D
 E E E E E
 Here n=5
Platform:
 - Striver's sheet

Topic:
 - Character Printing
 - Understanding incrementing in characters

Difficulty:
 - Medium

Approach:
-The Pattern prints a right-angled triangle of alphabets where each row contains
the same character.

 - variable p is initialized to 65 the ascii of A outside the outerloop to have it once and static
 - The outer loop runs form i=0 to n-1
 - The inner loop prints the character from j=0 to i+1 ( increasing triangle)
 - Outside outer loop incrementation is done so as to increase it every row and keep the alphabes same in each row
 - print() for new line

Time Complexity:
- O(N^2), because the total number of characters printed is the sum of the first N natural numbers

Space Complexity:
- O(1)

Date Solved:
- 17 Aug 2026

Mistake:
- Kept Print ()  Outside

Key Takeaway:
- Character incrementation can be done row by row through keeping the (initialization variable)p outside the outer loop

Revision:
[ ] Rev 1
[ ] Rev 2
[ ] Rev 3
"""


class Solution:

    def solve(self,n):
        #keeping the character initialization to ascii value of A, keeping it outside to incrementing only once
        p=65
        for i in range(n):
            for j in range(i+1):
                print(chr(p), end=" ")
            #Increment inside outer loop so that character can  increase after every cycle and starts from new line with new character
            p +=1
            print()

if __name__ == "__main__":
    solution = Solution()

    # Test your solution here
    n=5
    solution.solve(n)
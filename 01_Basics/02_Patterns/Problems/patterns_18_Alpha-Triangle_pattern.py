"""
Problem:
- Given an integer N, print the following pattern :
 E
 D E
 C D E
 B C D E
 A B C D E
 HERE N = 5
Platform:
Striver's sheet


Topic:
- Printing alphabets in reverse

Difficulty:
-medium

Approach:
-
- The goal is to print a pattern of alphabets where row starts with letter and moves down to A as we go down the row
   - initialize a variable outside so that it can be decremented to have a new letter each row to start with
   -loop through each row i = 0 to n-1
   - initialize another variable k=p which will be helpful to print the pattern column wis
   - in inner loop print the k and then keep on adding so that it reaches the final E's index
   - subtact the first variable outside the inner loop to 03_set it one less so in inner loop in next round we progress upto our desired letter
Time Complexity:
- O(N^2)

Space Complexity:
- O(1)

Date Solved:
-17- Aug-2026

Mistake:
- Struggling with how to print the reverse of the alphabets

Key Takeaway:
- Use two variables, one that shifts the starting of each row, and another that resets and count up within in each row
- I can write ord("E") instead of remembering the ascii value to put it in variable p.
Revision:
[ ] Rev 1
[ ] Rev 2
[ ] Rev 3
"""


class Solution:

    def solve(self,n):
        #varible to initialize to ascii 69 and have it reduced every row
        p = ord("E")
        for i in range(n):
            #variable to keep the column wise printing
            k=p
            for j in range(i+1):

                print(chr(k), end=" ")
                #increase upto desired letter's index
                k +=1
            #Decrease to start from one lesser index
            p -=1
            print()


if __name__ == "__main__":
    solution = Solution()

    # Test your solution here'
    n=5
    solution.solve(n)
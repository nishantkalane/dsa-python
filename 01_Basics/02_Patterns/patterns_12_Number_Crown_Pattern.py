"""
Problem:
- Given and Integer N, Print the following Pattern:
  1                 1
  1 2             2 1
  1 2 3         3 2 1
  1 2 3 4     4 3 2 1
  1 2 3 4 5 5 4 3 2 1
Platform:
- Striver's

Topic:
- Counting down rightfully row wise

Difficulty:
- Medium

Approach:
- This pattern prints a mirrored sequence of numbers on both sides with spaces in the center. The outer digits increase and decrease symmetrically,
while the center gap shrinks with each row, forming a diamond-like structure across rows.

-Identify the number and the sequence in which it will need incrementing and decrementing triangles,
-loop from 1 to N to handle each row
-Initialize p inside outer loop to have the each starting of the row to a particular row
-Decrement or increment p inside the inner loop to hav ea increasing or decreasing patter
-to not have clash remove one one column from the empty space triangles
-Incrementation will happen the first time then the decrementation and it will happen before prinitng so as to repeat the last number and have 1 at the end
Time Complexity:
- O(N^2)

Space Complexity:
- O(1)

Date Solved:
- 26/08/2026

Mistake:
- Was not incrementing properly for the second side of the crown
Key Takeaway:
- Incrementing can be done properly if we want the mirror by subtracting beforehand of print the second time

Revision:
[ ] Rev 1
[ ] Rev 2
[ ] Rev 3
"""


class Solution:

    def pattern_12(self,n):

        for i in range(n):
            p=1

            for j in range(i+1):
                print(p, end= " ")
                p+=1

            for j in range(i,n-1):
                print(" ", end= " ")
            for j in range(i,n-1):
                print(" ", end= " ")
            for j in range(i+1):
                p=p-1
                print(p, end= " ")
            print()
if __name__ == "__main__":
    solution = Solution()

    # Test your solution here
    N=5
    solution.pattern_12(N)
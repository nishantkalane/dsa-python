"""
Problem:
- Given and Integer N, Print the following Pattern:
  A
  A B
  A B C
  A B C D

Platform:
-Stiver

Topic:
-Printing Character Patterns

Difficulty:
-easy

Approach:
- This pattern prints letters in a triangular format where each row starts from 'A' and goes up to a certain alphabet depending on the row number.
  The idea is to print the incrementing alphabets

- Loop from i to n to print the rows
- initlaize p=65, aasci equivalent of A inside the outer loop as we want to print it again from begining in a new row
- in inner loop print from i to n, print chr(p) this funciton gives the letter at that index
- increment p inside the inner loop to print the incrementing pattern of alphabet
- use print() to skip to the next line

Time Complexity:
-O(N^2)
Space Complexity:
-O(1)

Date Solved:
- 16-Aug-2026

key learning:
- ascii A= 65  , a = 97, 0 =48
- use chr(ascii) function to print the letter at particular ascii index

Revision:
[ ] Rev 1
[ ] Rev 2
[ ] Rev 3
"""


class Solution:

    def solve(self,n):

        for i in range(n):
            p = 65
            for j in range(i+1):
                print(chr(p), end=" ")
                p=p+1


            print()


if __name__ == "__main__":
    solution = Solution()

    # Test your solution here
    n=5
    solution.solve(n)

    # Test your solution here
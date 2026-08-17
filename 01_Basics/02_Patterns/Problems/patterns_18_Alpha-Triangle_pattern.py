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

Time Complexity:
-

Space Complexity:
-

Date Solved:
-

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
        p = ord("E")
        for i in range(n):
            k=p
            for j in range(i+1):
                print(chr(k), end=" ")
                k +=1
            p -=1
            print()


if __name__ == "__main__":
    solution = Solution()

    # Test your solution here'
    n=5
    solution.solve(n)
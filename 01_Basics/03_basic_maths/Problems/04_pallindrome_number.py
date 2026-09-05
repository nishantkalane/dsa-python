"""
Problem:
Check the pallindrome of a number
N=121
output: True
N=123
output: False

Platform:
Strivers sheet

Topic:
pallindrome of a number

Difficulty:
easy

Approach:
- Initialize rev_no to 0
- Duplicate the n
- start a while loop while n > 0
- get the last digit by modulo 10 of a number
- multiply the rev_no by 10 and add the last digit
-  divide by 10 to remove the last digit fraction part by converting it into int
- print true if rev_no is equal to dup  else false

Time Complexity:
O(log10N + 1), as in the worst case when N is a multiple of 10 the number of digits in N is log10 N + 1.
In the while loop we divide N by 10 until it becomes 0 which takes log10N iterations.
In each iteration of the while loop we perform constant time operations like modulus and division and pushing elements into the vector.

Space Complexity:
O(1), as only a constant amount of additional memory for the reversed number regardless of size of the input number.

Date Solved:
-05-SEP-2026

Mistake:
- forgot to cast the decreasing number

Key Takeaway:
- Remember to duplicate the n so to use to compare later

Revision:
[ ] Rev 1
[ ] Rev 2
[ ] Rev 3
"""

class Solution:

    def solve(self,n):

        dup=n
        rev_no=0
        while n>0:
            last_digit= n%10
            rev_no=(rev_no *10)+last_digit
            n=int(n/10)
        if rev_no ==dup:
            print("True")
        else:
            print("False")


if __name__ == "__main__":
    solution = Solution()

    # Test your solution
    inp=123
    solution.solve(inp)

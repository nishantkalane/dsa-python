"""
Problem:
Reverse a number
N=1234
output: 4321

Platform:
Strivers sheet

Topic:
Reversing a string

Difficulty:
easy

Approach:
- Initialize rev_no to 0
- start a while loop while n > 0
- get the last digit by modulo 10 of a number
- multiply the rev_no by 10 and add the last digit
-  divide by 10 to remove the last digit fraction part by converting it into int
- print rev_no

Time Complexity:
O(log10N + 1), as in the worst case when N is a multiple of 10 the number of digits in N is log10 N + 1.
In the while loop we divide N by 10 until it becomes 0 which takes log10N iterations.
In each iteration of the while loop we perform constant time operations like modulus and division and pushing elements into the vector.

Space Complexity:
O(1), as only a constant amount of additional memory for the reversed number regardless of size of the input number.

Date Solved:
-05-SEP-2026

Mistake:
- Duplicate of n is necessary as n eventually becomes 0 so it can't be used for comparing

Key Takeaway:
- Remember to add the rev_no= (rev_no * 10 ) + lastdigit

Revision:
[ ] Rev 1
[ ] Rev 2
[ ] Rev 3
"""

class Solution:

    def solve(self,n):

        rev_no=0
        while n>0:
            last_digit = n %10
            rev_no=(rev_no*10)+last_digit
            n =int(n/10)
        print(rev_no)


if __name__ == "__main__":
    solution = Solution()

    # Test your solution
    inp=1234
    solution.solve(inp)

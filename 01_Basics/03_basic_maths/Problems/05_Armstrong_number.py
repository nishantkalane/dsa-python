"""
Problem:
Check if the number is armstrong or not ( power of length of number, that  do the power of individual digits and then their sum is equal to the digit)
N= 371
output: True
N=123
output: False

Platform:
Strivers sheet

Topic:
armstrong number

Difficulty:
easy

Approach:
- keep the power to len(str(n))
- new no= 0
- Duplicate the n
- start a while loop while n > 0
- get the last digit by modulo 10 of a number
- power up the last digit to the length of n and then add it to the new no.
-  divide by 10 to remove the last digit fraction part by converting it into int
- print true if new number is equal to the dup, else false

Time Complexity:
O(log10N + 1) where N is the input number.
The time complexity is determined by the number of digits in the input integer N.
In the worst case when N is a multiple of 10 the number of digits in N is log10 N + 1.

Space Complexity:
O(1) as only a constant amount of additional memory for the reversed number regardless of size of the input number.

Date Solved:
-05-SEP-2026

Mistake:
- did not riase the last digit properly in armstrong number we have to raise the digit to the number equal to it's length
- did not typecast the n before calculating it's length for the power

Key Takeaway:
- Take the length of the digit to increase it to a certain power

Revision:
[ ] Rev 1
[ ] Rev 2
[ ] Rev 3
"""

class Solution:

    def solve(self,n):
        dup=n
        new_number=0
        power=len(str(n))
        while n >0:
            last_digit=n%10
            new_number +=(last_digit**power)
            n=int(n/10)
        if new_number == dup:
            print("True")
        else:
            print("False")


if __name__ == "__main__":
    solution = Solution()

    # Test your solution
    inp=123#try 1634 as well or 371
    solution.solve(inp)

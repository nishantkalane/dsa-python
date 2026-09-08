"""
Problem:
Extraction of digits
N=1234
print:
4
3
2
1

Platform:
Strivers sheet

Topic:
Extracting digits in reverse order

Difficulty:
easy

Approach:
- start a while loop while n > 0
- take the modulo to extract the last digit
- and divide by 10 to remove the last digit fraction part by converting it into int
- equal the n to the new number

Time Complexity:
- O(log n) removes one digit per iteration

Space Complexity:
- O(1) we use few variables

Date Solved:
-05-SEP-2026

Mistake:
- forgot to conver new number into int

Key Takeaway:
- Take Modulo by 10 for extracting last digit, and divide by 10 to remove last digit


"""


class Solution:

    def solve(self,n):
            while n>0:
                last_digit= n %10
                print(last_digit)
                new_digit =int(n/10)
                n = new_digit


if __name__ == "__main__":
    solution = Solution()

    # Test your solution
    inp=12345678
    solution.solve(inp)

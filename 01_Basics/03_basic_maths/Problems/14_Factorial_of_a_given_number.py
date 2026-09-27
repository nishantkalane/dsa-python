"""
Problem:
You are given an integer n. Return the value of n! or n factorial.
Factorial of a number is the product of all positive integers less than or equal to that number.

Example 1:
Input: n = 2
Output: 2

Explanation:
2! = 1 * 2 = 2.
Example 2:
Input: n = 0
Output: 1

Explanation: 0! is defined as 1.

Platform:
DSA sheet

Topic:
Number properties

Difficulty:
medium

Approach:
Initialize fac=1
if n = 0, return 1.
loop from 1 to n and multiply each number into fac.
return fac.


Time Complexity: O(n).

Space Complexity: O(1).

Date Solved:
-27-SEP-2026

Mistake: initialize fac to 1 and not 0
Key Takeaway:Factorial: n! = 1 × 2 × 3 × ... × n, and 0! = 1.
initialize fac to 1 and not 0
"""


class Solution:

    def solve(self, n):
        fac=1
        if n == 0:
            return 1
        else:
            for i in range(1,n+1):
                fac *=i
            return fac

if __name__ == "__main__":
    solution = Solution()

    # Test your solution
    inp = int(input())
    result = solution.solve(inp)
    print(result)

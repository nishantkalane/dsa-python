"""
Problem:
Problem Statement: Given a number ‘N’, find out the sum of the first N natural numbers .

Input: N=5
Output: 15
Explanation: 1+2+3+4+5=15

Input: N=6
Output: 21
Explanation: 1+2+3+4+5+6=15

Platform:
Strivers sheet

Topic:
Number properties

Difficulty:
medium

Approach:
We can use the formula for the sum of N numbers, i.e N(N+1)/2.
Take a variable sum.
Initialize it with N(N+1)/2, where N is a given number.

Time Complexity: O(1).

Space Complexity: O(1).

Date Solved:
-13-SEP-2026

Mistake:
Key Takeaway:
formula to get sum of all numbers till n natural number is (N*(N+1))//2

"""


class Solution:

    def solve(self, n):
        return (n*(n+1))//2





if __name__ == "__main__":
    solution = Solution()

    # Test your solution
    inp = int(input())
    result = solution.solve(inp)
    print(result)

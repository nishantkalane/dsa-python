"""
Problem:

Platform:
DSA Sheet

Topic:
Functional Recursion

Difficulty:
medium

Approach:
Base Case: if n ==0, return 1.
Recursive case: return n * solve(n-1)
continue until n=0


Time Complexity: O(N), one recursive call for each value from n to 0
Space Complexity : O(N), recursion stack stores n calls
Date Solved:
-27-SEP-2026

Key Takeaway:
Factorial using recursion: n! = n × (n-1)!, with 0! = 1.
and see that recursive call is made perfectly with deduction

"""


class Solution:

    def solve(self, n):
        if n== 0:
            return 1
        return n* self.solve(n-1)


if __name__ == "__main__":
    solution = Solution()

    # Test your solution
    inp = 7
    result = solution.solve(inp)
    print(result)

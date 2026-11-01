"""
Problem:
Input: N=5
Output: 15
Explanation: 1+2+3+4+5=15

Input: N=6
Output: 21
Explanation: 1+2+3+4+5+6=15

Platform:
DSA Sheet

Topic:
Functional Recursion

Difficulty:
medium

Approach:
Instead of looping, we can solve the problem using recursion by defining the sum of the first N natural numbers as:

sum(N) = N + sum(N-1), with the base case sum(1) = 1.

Recursive way of calculating the sum of first N Natural Numbers:
 Define a recursive function to calculate the sum of natural numbers.
 If the input is the smallest natural number, return it directly as the base case.
 Otherwise, add the current number to the result of calling the same function with the previous number.
 Repeat this process until the base case is reached.
 The results from each call combine to give the final sum.


Time Complexity: O(N), as we iterate from 1 to N performing constant-time operation for each iteration.
Space Complexity : O(1), as the space used by the algorithm does not increase with the size of the input..

Date Solved:
-14-SEP-2026

Mistake:
Key Takeaway:
make sure to return when it's 0 in base condition and in else block make sure  to call the recursive function by reducing the n



"""


class Solution:

    def solve(self, n):
        if n==0:
            return
        return n+self.solve(n-1)


if __name__ == "__main__":
    solution = Solution()

    # Test your solution
    inp = 6
    result = solution.solve(inp)
    print(result)

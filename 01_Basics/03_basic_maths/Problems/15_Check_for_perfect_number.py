"""
Problem:
You are given an integer n. You need to check if the number is a perfect number or not. Return true if it is a perfect number, otherwise, return false.
A perfect number is a number whose proper divisors (excluding the number itself) add up to the number itself.

Example 1:
Input: n = 6
Output: true
Explanation: Proper divisors of 6 are 1, 2, 3.
1 + 2 + 3 = 6.

Example 2:
Input n = 4
Output: false
Explanation: Proper divisors of 4 are 1, 2.
1 + 2 = 3.

Platform:
DSA sheet

Topic:
Number properties

Difficulty:
Easy

Approach:
Iterate i from 1 to √n.
If i divides n, both i and n/i are factors.
Add the factors to sum, avoiding duplicates and excluding n itself.
Finally, check if sum == n.
If yes → Perfect Number.

Time Complexity: O(underoot of n).

Space Complexity: O(1).

Date Solved:
-28-SEP-2026

Mistake: see that n //  i !=n doesn't count the n as a divisor in our way as perfect number just has pure divisors and not n

Key Takeaway:
For divisor problems, iterate only up to √n and pair factors using i and n/i and missing n by the condition n/i is not equal to n.
"""


class Solution:

    def solve(self, n):
        sum=0
        i=1
        while i*i <=n:
            if n % i ==0  :
                sum +=i
                if n//i !=i and n //i != n:
                    sum+=n//i
            i +=1
        if sum == n:
            return True
        return False


if __name__ == "__main__":
    solution = Solution()

    # Test your solution
    inp = int(input())
    result = solution.solve(inp)
    print(result)

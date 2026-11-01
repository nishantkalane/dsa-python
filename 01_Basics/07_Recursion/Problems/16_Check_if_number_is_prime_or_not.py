"""
Problem:
Check whether a number is prime using recursion by checking whether it has any divisor other than 1 and itself.

Platform:
DSA Sheet

Topic:
Recursion-> Prime Number -> Divisibility

Difficulty:
Easy

Approach:
- Start Checking divisors form div =2
- if div > under-root of n, no divisor was found, so return True.
- Check whether n%div ==0.
- If divisible, return False because n is not prime.
- Otherwise, recursively check the next divisor using div +1.
- Continue until a divisor is found or under roo tof n is crossed

Time Complexity:
- O(under root of n) -> Checks divisors only up to under root of n.

Space Complexity:
- O(under root of n)-> recursive calls create as tack up to under root of n

Date Solved:
- 2 oct 2026

Mistake:
- solved with basic math approach while there was a better approach

Key Takeaway:
To check primality, only test divisors from 2 to under-root n. if any divisor divides n, it is not prime.

-

"""
import math


class Solution:

    def solve(self,div,n):
        if div > math.sqrt(n):
            return True
        if n % div ==0:
            return False
        return self.solve(div+1, n)



if __name__ == "__main__":
    solution = Solution()

    # Test your solution here
    inn=int(input("Enter a number to check weather it's a prime or not : "))
    print(solution.solve(2,inn))
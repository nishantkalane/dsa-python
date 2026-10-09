"""
Problem:
You are given two positive integers a and b. You need to find their Least Common Multiple (LCM).
The LCM is the smallest positive integer that is divisible by both a and b.

Example 1:
Input: a = 4, b = 6
Output: 12

Explanation:
Multiples of 4 are 4, 8, 12, 16...
Multiples of 6 are 6, 12, 18...
The smallest common multiple is 12.

Example 2:
Input: a = 12, b = 18
Output: 36

Explanation:
The GCD of 12 and 18 is 6.
Using:
LCM(a, b) = (a × b) / GCD(a, b)
LCM = (12 × 18) / 6 = 36

Platform:
DSA Sheet

Topic:
Basic Maths/ Number Properties

Difficulty:

Approach:
-medium

Time Complexity:
- O(log(min,a,b)

Space Complexity:
- o(1)

Date Solved:
-8 oct 2026

Mistake:
-Initially, I needed to understand how a, b = b, a % b works. It simultaneously updates both variables by moving b into a and the remainder of a % b into b.

Key Takeaway:
LCM can be efficiently calculated using the relation:
LCM(a, b) = (a × b) / GCD(a, b)
The GCD can be found efficiently using the Euclidean Algorithm:
-

"""


class Solution:
    def gcd(self,ma, mb):
        while mb != 0:
            ma, mb = mb, ma % mb
        return ma
    def lcm(self,a,b):
        return (a*b) // self.gcd(a,b)


if __name__ == "__main__" :
    sol= Solution()

    aa= int(input("Enter a: "))
    bb = int(input(("Enter b:")))

    print(sol.lcm(aa,bb))
# TC= O(log(n))
# SC= O(1)
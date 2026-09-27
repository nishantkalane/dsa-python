"""
Problem:
You are given an integer n. You need to find out the number of prime numbers in the range [1, n] (inclusive). Return the number of prime numbers in the range.
A prime number is a number which has no divisors except, 1 and itself.

Example 1:
Input: n = 6
Output: 3
Explanation: Prime numbers in the range [1, 6] are 2, 3, 5.

Example 2:
Input: n = 10
Output: 4
Explanation: Prime numbers in the range [1, 10] are 2, 3, 5, 7.


Platform:
DSA sheet

Topic:
Number properties

Difficulty:
medium

Approach:
Iterate through every number m from 1 to n.
for each m, count it's divisors using i up to underoot of m
if m has exactly 2 divisors it is prime.
increment prime count.
return total number of primes.


Time Complexity: O(nrootn)- for each number, check divisors up to under root of n.

Space Complexity: O(1) only counters and vaiables are used

Date Solved:
-28-SEP-2026

Mistake:
use the while loop of under root check and the second if condition properly
Key Takeaway:
A prime number has exactly 2 divisors: 1 and itself.
Use the √n divisor-checking technique to reduce unnecessary checks.
"""


class Solution:

    def solve(self, n):
        prime_count =0
        for m in range(1,n+1):
            cnt = 0
            div=[]
            i=1
            while i*i <= m+1:
                if m % i ==0:
                    cnt +=1
                    if m // i !=i:
                        cnt +=1
                i +=1
            if cnt ==2:
                prime_count+=1
        return prime_count




if __name__ == "__main__":
    solution = Solution()

    # Test your solution
    inp = int(input())
    result = solution.solve(inp)
    print(result)

"""
Problem:
Find the nth Fibonacci number using recursion. Each Fibonacci number is the sum of the previous two numbers.
n=4
output=3
n=6
output = 8

Platform:
DSA Sheet

Topic:
Recursion -- Fibonacci

Difficulty:
medium

Approach:
1. If n <=1, return n because F(0)=0 and f(1) =1.
2. Recursively calculate the previous Fibonacci number using solve(n-1)
3. Recursively calculate the second previous Fibonacci number using solve(n-2).
4. Add both results to get the fibonacci number at position n.
5. Retrun the calculated value


Time Complexity: O(2^n) Each call creates two more recursive calls, causing repeated calculations
Space Complexity : O(n) Maximum recursion depth is n.


Date Solved:
-30-SEP-2026

Mistake:
You don't need to take index, directly take n and then deduct it for last and second last

Key Takeaway:
F(n)= F(n-1) + F(n-2), with base cases F(0) = 0 and F(1)= 1)

"""


class Solution:

    def solve(self, n):
        if n <=1:
            return n
        last= self.solve(n-1)
        second_last=self.solve(n-2)
        return last+second_last

if __name__ == "__main__":
    solution = Solution()

    # Test your solution
    inp=int(input("Enter a number place at which number in fibomaic series: "))
    result = solution.solve(inp)
    print(result)

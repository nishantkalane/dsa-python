"""
Problem:
Get the GCD or HCF of two numbers
input: n1=9 and n2=12
output: 3

Platform:
Strivers sheet

Topic:
GCD, HCF

Difficulty:
medium

Approach:

1. Approach 1: Increasing Order
Intuition:
The GCD is the largest common factor. Check every number from 1 to min(n1,n2). Whenever i is a common factor, update gcd. The last common factor found is the GCD.
Algorithm:
1. Initialize gcd = 1.
2. Iterate i from 1 to min(n1,n2).
3. If i divides both numbers, set gcd = i.
4. Return gcd.
TC: O(min(n1,n2))
SC: O(1)

2. Approach 2: Decreasing Order
Intuition:
Start from min(n1,n2), the largest possible GCD, and move downward. The first common factor found is the GCD, so we can return immediately.
Algorithm:
Instead of checking every possible factor and keeping track of the largest one, we stop as soon as we find the first common factor. Since we are checking from largest to smallest, the first common factor we encounter is guaranteed to be the GCD.

1. Set i = min(n1,n2).
2. Iterate downward to 1.
3. If i divides both numbers, return i.
4. If none is found, return 1.
TC: O(min(n1,n2)) worst case
SC: O(1)

Date Solved:
-07-SEP-2026

Mistake:
- use and not & in python
- use less than equal to in while loop as minimum is also included
-keeping the minimum greater than equal to one in better approach
Key Takeaway:
- use and not & in python
- use less than equal to in while loop as minimum is also included
-keeping the minimum greater than equal to one in better approach


"""


class Solution:

    def solve(self, n1,n2):
        i=1
        minimum =min(n1,n2)
        gcd=1
        while minimum >= 1:
            if n1 % i == 0 and n2 % i ==0:
                gcd= i
            minimum -=1
        return gcd




if __name__ == "__main__":
    solution = Solution()

    # Test your solution
    inp1 = 4
    inp2 = 9
    result = solution.solve(inp1,inp2)
    print(result)

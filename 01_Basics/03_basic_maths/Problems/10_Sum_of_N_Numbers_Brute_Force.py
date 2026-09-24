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
The most straightforward way to find the sum of the first N natural numbers is to iterate from 1 to N and keep adding each number to a running total.
This approach is beginner-friendly and easy to understand because it directly mimics the problem definition.
However, it is less efficient than the formula-based approach since it requires looping through all numbers, which means more time complexity when N is large.

 -Initialize a variable to store the sum as 0.
 -Start a loop from 1 and go up to the given number.
 -In each iteration, add the current number to the sum.
 -After the loop finishes, the sum variable will hold the result.
 -Return or print the sum

Time Complexity: O(N),We iterate from 1 to N once, performing a constant-time addition operation in each iteration, resulting in linear time complexity.

Space Complexity: O(1),We only use a few variables to store the sum and loop counter, so the space usage remains constant regardless of N.

Date Solved:
-13-SEP-2026

Key Takeaway:
    check the range function properly range(n) n is inculsive and in range(1,n) n is exclusive


"""


class Solution:

    def solve(self, n):
        total =0
        for i in range(n):
            total += i
        return total





if __name__ == "__main__":
    solution = Solution()

    # Test your solution
    inp = 3
    result = solution.solve(inp)
    print(result)

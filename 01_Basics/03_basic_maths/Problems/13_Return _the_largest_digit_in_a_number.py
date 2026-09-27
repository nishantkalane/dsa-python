"""
Problem:
You are given an integer n. Return the largest digit present in the number.

Example 1:
Input: n = 25
Output: 5
Explanation: The largest digit in 25 is 5.

Example 2:
Input: n = 99
Output: 9
Explanation: The largest digit in 99 is 9.

Platform:
DSA sheet

Topic:
Digit Manipulation

Difficulty:
easy

Approach:
Extract last digit using n % 10.
Compare it with maximum.
Update maximum if the digit is greater.
Remove last digit using n // 10.
Repeat until n = 0.

Time Complexity: O(log n).

Space Complexity: O(1).

Date Solved:
-27-SEP-2026


Key Takeaway:
Use % 10 to extract each digit and maintain a running maximum.
"""


class Solution:
    def solve(self, n):
        maximum=0
        while n > 0 :
            last_digit = n % 10
            if last_digit > maximum:
                maximum=last_digit
            n= n //10
        return maximum


if __name__ == "__main__":
    solution = Solution()

    # Test your solution
    inp = int(input())
    result = solution.solve(inp)
    print(result)

#TC= O(log(n)) process each digit once
#SC = O (1) constant extra space
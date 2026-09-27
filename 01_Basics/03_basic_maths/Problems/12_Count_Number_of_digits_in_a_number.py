"""
Problem:
Problem Statement: You are given an integer n. You need to return the number of odd digits present in the number.

Example 1:
Input: n = 5
Output: 1
Explanation: 5 is an odd digit.

Example 2:
Input: n = 25
Output: 1
Explanation: The only odd digit in 25 is 5.

Platform:
DSA sheet

Topic:
Digit Manipulation

Difficulty:
easy

Approach:
we loop while there are digits in a number
take out the last digit
Using a condition weather it is not divisible by 2 and it is not 2 , if so we increase the counter of odd number
we remove one digit from the number
print the odd count

Time Complexity: O(log n).

Space Complexity: O(1).

Date Solved:
-27-SEP-2026

Mistake:
you can directly check odd by divisibility by 2 and no need to use brute force approach

Key Takeaway:
% 10 → get digit | // 10 → remove digit | % 2 → check odd/even.

"""


class Solution:
    def solve(self, n):
        cnt=0
        while n>0:
            last_digit = n % 10
            if last_digit % 2 != 0 and last_digit !=2:
                cnt +=1
            n = n //10
        return cnt


if __name__ == "__main__":
    solution = Solution()

    # Test your solution
    inp = int(input())
    result = solution.solve(inp)
    print(result)

#TC= O(log(n)) process each digit once
#SC = O (1) constant extra space
"""
Given a numeric string, find the largest-valued odd number that is a non-empty prefix of the string.

Example: num = "35427"
Output: "35427"

Platform:
LeetCode

Topic:
String Manipulation

Pattern:
Reverse Traversal / Greedy / String Slicing

Difficulty:
Easy

Approach:
- Start traversing the string from right to left.
- Check whether the current digit is odd using int(num[i]) % 2 != 0.
- When the first odd digit is found, return the substring num[:i+1].
- If no odd digit is found, return an empty string.

Time Complexity:
- O(n), worst-case traversal of the entire string.

Space Complexity:
- O(n), for the returned substring in Python.

Date Solved: 3 nov
Mistake:

- Forgot to return an empty string when no odd digit was found.

Key Takeaway:

- For finding the largest odd prefix, locate the rightmost odd digit and extract the prefix ending at that position.
"""

class Solution:
    def solve(self,num):
        for i in range(len(num)-1,-1,-1):
            if int(num[i]) % 2 !=0:
                result = num[:i+1]
                return result.lstrip("0")
        #case in situations of no odd digit
        return ""



if __name__ == "__main__":
    sol = Solution()

    num= "054212543"
    print(sol.solve(num))
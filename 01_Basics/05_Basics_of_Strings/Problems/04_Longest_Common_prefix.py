
"""
Problem:

Given an array of strings, find the longest common prefix shared by all strings.

Example: strs = ["flower", "flow", "flight"]
Output: "fl"

Platform:
LeetCode / Striver's Sheet

Topic:
String Comparison

Pattern:
Vertical Scanning / Nested Loops

Difficulty:
Easy

Approach:
- Find the length of the shortest string.
- Traverse the strings character by character using an outer loop.
- Compare characters at the same index across all strings using an inner loop.
- If a mismatch occurs, return the prefix collected so far.
- Otherwise, append the matching character to the prefix.
- Return the prefix after completing the traversal.
Time Complexity:

- O(n × m), where n is the number of strings and m is the length of the shortest string.

Space Complexity:

- O(m), for storing the resulting prefix.
Date Solved: 3 nov 2026
Mistake:

- Initially placed the prefix append operation inside the inner loop instead of after all strings were checked.

Key Takeaway:

- Vertical scanning compares characters at the same index across multiple strings to identify their common prefix.

"""
class Solution:
    def solve(self,num):
        prefix = ""
        min_len = min(len(s) for s in num)
        for j in range(min_len):
            for i in range(len(num)):
                if num[i][j] != num[0][j]:
                    return prefix
            prefix +=num[0][j]
        return prefix

if __name__ == "__main__":
    sol = Solution()

    strs = ["flower", "flow", "fly", "flight"]
    print(sol.solve(strs))
"""
Problem:

Given two strings s and t, determine whether t is an anagram of s. Both strings must contain exactly the same characters with identical frequencies.

Example: s = "anagram", t = "nagaram"
Output: True

Platform:
LeetCode / Striver's Sheet

Topic:
Hashing / String Manipulation

Pattern:
Frequency Counting / Hash Map (Dictionary)

Difficulty:
Easy

Approach:
- First check whether both strings have equal lengths. If not, return False.
- Create two empty dictionaries to store character frequencies.
- Traverse string s and count the frequency of each character.
- Traverse string t and count the frequency of each character.
- Compare both dictionaries.
- If both dictionaries are equal, return True; otherwise, return False.
Time Complexity:

- O(n), traverse both strings.

Space Complexity:

- O(1), because the constraints allow only 26 lowercase English letters.

Date Solved: 4 nov 2026
Mistake:
- Initially forgot to return the final comparison result.
- Used uppercase and lowercase characters in the test case, overlooking Python's case sensitivity.
Key Takeaway:

- Anagrams contain identical character frequencies. Use a dictionary to count and compare character occurrences
"""

class Solution:
    def solve(self,s,t):
        if len(s) != len(t):
            return False
        frequency_s = {}
        for char in s:
            frequency_s[char] = frequency_s.get(char, 0) + 1
        frequency_t = {}
        for char in t:
            frequency_t[char] = frequency_t.get(char, 0) + 1
        return frequency_t == frequency_s
if __name__ == "__main__":
    sol = Solution()
    s ="paper"
    t="repan"
    print(sol.solve(s,t))
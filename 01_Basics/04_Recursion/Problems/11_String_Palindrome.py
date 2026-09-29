"""
Problem:
Given a string s, return true if the string is palindrome, otherwise false.
A string is called palindrome if it reads the same forward and backward.

Example 1:
Input : s = "hannah"
Output : true
Explanation : The string when reversed is --> "hannah", which is same as original string , so we return true.

Example 2:
Input : s = "aabbaA"
Output : false
Explanation : The string when reversed is --> "Aabbaa", which is not same as original string, So we return false.

Platform:
DSA Sheet

Topic:
Recursion -- Palindrome/ Pointer Approach

Difficulty:
medium

Approach:
Start from the first character using index i = 0.
Compare st[i] with the corresponding character from the end, st[m-i-1].
If both characters are different, the string is not a palindrome, so return False.
If they are the same, recursively move to the next character by calling solve(i+1, st, m).
Continue comparing characters while moving towards the center.
Once i >= m//2, all required pairs have been matched, so return True.

Time Complexity: O(N), each character is checked at most once.
Space Complexity : O(1), recursion stack.


Date Solved:
-29-SEP-2026

Mistake: No major mistake, the condition i>=  m//2 correctly stops once the middle is reached

Key Takeaway:
For a recursive palindrome check, compare the first and last characters, then move pointers towards the center


"""


class Solution:

    def solve(self, i, st,m):
        if i >=m//2:
            return True
        if st[i] != st[m-i-1]:
            return False
        return self.solve(i+1,st,m)
if __name__ == "__main__":
    solution = Solution()

    # Test your solution
    string_is = "hannah"
    n=len(string_is)
    result = solution.solve(0,string_is,n)
    print(result)

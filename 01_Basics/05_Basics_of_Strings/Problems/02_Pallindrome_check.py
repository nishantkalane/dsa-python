"""
Problem:

Check whether a given string reads the same forward and backward.

Example: s = "madam"
Output: True

Platform:
Striver's Sheet

Topic:
String Manipulation

Pattern:
Two Pointers / Symmetrical Comparison

Difficulty:
Easy

Approach:
- Initialize two pointers at the beginning and end of the string.
- Compare the characters at both pointers.
- If they are different, return False.
- Move the pointers towards the centre.
- If all characters match, return True.
Time Complexity:

- O(n), traverse half the string.

Space Complexity:
- O(1), use only two pointers.

Date Solved: 2 nov 2026

Mistake: --
Key Takeaway:
- Compare characters from opposite ends to check whether a string is symmetrical.
"""


class Solution:
    def reverseString(self, s):
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] !=s[r]:
                return False
            l +=1
            r -=1

        return True
if __name__ == "__main__":
    sol = Solution()

    st="adba"
    string_list= list(st)
    r= sol.reverseString(string_list)
    print(r)
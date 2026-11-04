"""Problem:

Reverse the given string.

Example: s = "hello"
Output: "olleh"

Platform:
LeetCode / Striver's Sheet

Topic:
String Manipulation

Pattern:
Two Pointers / Swapping

Difficulty:
Easy

Approach:
- Initialize two pointers, left = 0 and right = len(s) - 1.
- Compare and swap the characters at both pointers.
- Increment left and decrement right.
- Continue until left >= right.

Time Complexity:
- O(n), traverse half the string.

Space Complexity:
- O(1) for in-place swapping in a mutable character array.
- O(n) if creating a new reversed string.

Date Solved: 2 Nov 2026

Mistake:

- Strings in Python are immutable, so direct character swapping on a string is not allowed.

Key Takeaway:

- Use two pointers to compare or swap characters from opposite ends.
"""



class Solution:
    def reverseString(self, s):
        l = 0
        r = len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        s = "".join(s)
        return s
if __name__ == "__main__":
    sol = Solution()

    st="Nishant"
    string_list= list(st)
    r= sol.reverseString(string_list)
    print(r)
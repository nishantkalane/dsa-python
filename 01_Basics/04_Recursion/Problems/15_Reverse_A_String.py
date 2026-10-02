"""
Problem:
Reverse a String I
Given an input string as an array of characters, write a function that reverses the string.

Example 1:
Input : s = ["h", "e", "l", "l", "o"]
Output : ["o", "l", "l", "e", "h"]
Explanation : The given string is s = "hello" and after reversing it becomes s = "olleh".

Example 2:
Input : s = ["b", "y", "e" ]
Output : ["e", "y", "b"]
Explanation : The given string is s = "bye" and after reversing it becomes s = "eyb".

Platform:
DSA Sheet

Topic:

Difficulty:

Approach:
-

Time Complexity:
-

Space Complexity:
-

Date Solved:
- 1 - OCT - 2026

Mistake:
-

Key Takeaway:
-

"""


class Solution:

    def solve(self,i,strr):
        n=len(strr)
        if i >=n//2:
            return "".join(strr)
        strr[i],strr[n-i-1] = strr[n-i-1], strr[i]
        return self.solve(i+1,strr)



if __name__ == "__main__":
    solution = Solution()

    # Test your solution here
    stre=input("Enter a string to reverse: ")
    str=list(stre)
    print(solution.solve(0,str))
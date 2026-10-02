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
Recursion -> String -> True

Difficulty:
-Easy
Approach:
-Start form the first character at index i=0.
-Compare the current position with its corresponding position form the end, n-i-1
-Swap these two characters.
-Recursively move to the next index using i +1
- Stop when i >= n//2, because all required swaps are completed
-  Join the character array and return the reversed string

Time Complexity:
- O (N) each character is processed at most once

Space Complexity:
- O(N) Recursion stack takes O(N) space

Date Solved:
- 1 - OCT - 2026

Mistake:
-conversion of string to list and list to string
Key Takeaway:
- Swap the firs and the last characters, turn sting in to list using list() and back in string using "".join(), do recursively move both ends towards the center

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

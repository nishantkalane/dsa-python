"""
Problem: Alpha-Hill Pattern
Given an integer N, print the following pattern:
      A
    A B A
  A B C B A
A B C D C B A
here n=5

Platform:
- Striver's sheet

Topic:
-Mixing of alphabets an hill pattern


Difficulty:
-easy

Approach:
- iterate from i=0 to n-1
- initialize p=65 for ascii character A
- in inner loop first create decrementing triangle
- In next inner loop print chr(p) character at p index
- Increment p in it so to print the increasing alphabets
_ In next inner loop print chr(p) character at p index
- Decrement p in it so to print the decreasing alphabets
- remove 1 row from middle of first triangle so  to have the hill top


Time Complexity:
- O(N^2)

Space Complexity:
- O(1)

Date Solved:
- 17-08-2026

Mistake:
- removing the right row

Key Takeaway:
- for the hill pattern in growing and decrementing pattern you first increment the variable and then decrement it in those respective inner loop.

Revision:
[ ] Rev 1
[ ] Rev 2
[ ] Rev 3


"""

class Solution:

    def solve(self,n):
        for i in range(n):
            p=65
            for j in range(i,n):
                print(" ", end=" ")
            for j in range (i):
                print(chr(p), end=" ")
                p +=1
            for j in range (i+1):
                print(chr(p), end=" ")
                p -=1
            print()


if __name__ == "__main__":
    solution = Solution()

    # Test your solution here
    n=6
    solution.solve(n)
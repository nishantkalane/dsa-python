"""
Problem:
Print from 1 to N using recursion
input=3
output : 1 2 3


Platform:
Striver

Topic:
Recursion

Type:
Travel recursion

Difficulty:
easy

Approach:

To print numbers from 1 to n using forward recursion,
the approach involves defining a recursive function that takes the current number as a parameter.
The function first checks if the current number exceeds n; if it does, the recursion terminates.
Otherwise, it prints the current number and then recursively calls itself with the next number incremented by one.
This way, the numbers are printed in ascending order as the recursion unfolds forward from the base case to the maximum number.
The key is to make the print statement before the recursive call, ensuring the numbers appear from 1 up to n in order.

Time Complexity: O(N), we print every number from 1 to N using recursion
Space Complexity: O(N), stack space used for recursive calls.

Date Solved:
- 9-Sep-2026

Key Takeaway:
- To make the forward recursion print the value before calling the recursive function
"""

class Solution:
    def solve(self,i,n):
        if i > n:
            return
        print(i)
        self.solve(i+1,n)


if __name__ == "__main__":
    solution = Solution()

    # Test your solution here
    inp = int(input("How many times you want to print a number? "))

    solution.solve(1,inp)



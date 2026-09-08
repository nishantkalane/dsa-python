"""
Problem:
Print from 1 to N using recursion
input=3
output : 3 2 1


Platform:
Striver

Topic:
Recursion

Type:
Travel recursion

Difficulty:
easy

Approach:

Define a recursive function solve(i, n) where i represents the current number to be printed and n represents the original input.
Start the recursion with i = n, so the first number printed is n.
Before making the recursive call, check the base case:- If i < 1, stop the recursion using return.

If the base condition is not satisfied, print the current value of i.
Then make the recursive call with i - 1, which decreases the number by 1 in every recursive call.
This continues until i becomes 0, at which point i < 1 becomes true and the recursion terminates.
Since the print(i) statement is placed before the recursive call, each number is printed immediately as the recursion moves forward.
Therefore, for n = 3, the execution produces:

Time Complexity: O(N), we print every number from 1 to N using recursion
Space Complexity: O(N), stack space used for recursive calls.

Date Solved:
- 9-Sep-2026

Key Takeaway:
In forward recursion, when you want to print numbers from n down to 1,
print the current value before making the recursive call and decrease the value by 1 in each call."""

class Solution:
    def solve(self,i,n):
        if i <1:
            return
        print(i)
        self.solve(i-1,n)


if __name__ == "__main__":
    solution = Solution()

    # Test your solution here
    inp = int(input("How many times you want to print a number? "))

    solution.solve(3,inp)



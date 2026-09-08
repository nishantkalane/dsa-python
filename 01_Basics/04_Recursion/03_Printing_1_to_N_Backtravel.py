"""
Problem:
Print from 1 to N using Backward recursion
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

Backtracking builds solutions by exploring all options and undoing choices when needed.
To print numbers from 1 to n using backtracking, the function recursively calls itself with the next number until it passes n.
After reaching the base case, it prints the numbers while returning from the recursion.
This way, numbers are printed in reverse order because the print happens after the recursive call during backtracking.
The main difference from forward recursion is that printing occurs on the way back, not before the recursive call.

Time Complexity: O(N), we print every number from 1 to N using recursion
Space Complexity: O(N), stack space used for recursive calls.

Date Solved:
- 9-Sep-2026
Mistake:
-Base condition i should be if i <1 and not if i >1 as we will be backtracking
Key Takeaway:
- To make the forward recursion print the value before calling the recursive function
"""

class Solution:
    def solve(self,i,n):
        if i < 1:
            return
        self.solve(i-1,n)
        print(i)

if __name__ == "__main__":
    solution = Solution()

    # Test your solution here
    inp = int(input("How many times you want to print a number? "))

    solution.solve(inp,inp)



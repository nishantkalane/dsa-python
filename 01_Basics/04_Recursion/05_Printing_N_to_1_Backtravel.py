"""
Problem:
Print from N to 1 using Backward recursion
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

- Define a recursive function `solve(i, n)` where `i` represents the **current number** and `n` represents the **maximum number up to which we want to print**.
- Start the recursion with `i = 1`, so the function begins from the smallest number.
- First, check the **base case**:
  - If `i > n`, stop the recursion using `return`.
- If the base condition is not satisfied, make the recursive call **before printing**:
  ```python
  self.solve(i + 1, n)
  ```
- In every recursive call, `i` is increased by `1`, so the recursion continues deeper until `i` becomes greater than `n`.
- At this point, the base case is reached and the function starts **returning back through the previous recursive calls**.
- The `print(i)` statement is placed **after the recursive call**, so the values are printed while the recursion is **backtracking**.
- Therefore, although the recursion initially travels forward as `1 → 2 → 3 → ... → n`, the printing happens while returning:
  ```text
  n → n-1 → n-2 → ... → 1
  ```

Time Complexity: O(N), we print every number from 1 to N using recursion
Space Complexity: O(N), stack space used for recursive calls.

Date Solved:
- 9-Sep-2026

Mistake:
in base condition check that i > n because we started from 1 so condition will stop when we will go over 1
Key Takeaway
In backtracking recursion, place the print statement after the recursive call. The recursion first travels forward to the base case, then prints the values while returning backward, producing `n` down to `1`.**
"""

class Solution:
    def solve(self,i,n):

        if i > n:
            return
        self.solve(i+1,n)
        print(i, end=" ")


if __name__ == "__main__":
    solution = Solution()

    # Test your solution here
    inp = int(input("How many times you want to print a number? "))
    solution.solve(1,inp)




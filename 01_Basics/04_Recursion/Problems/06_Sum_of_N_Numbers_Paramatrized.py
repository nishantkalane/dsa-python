"""
Problem:
Input: N=5
Output: 15
Explanation: 1+2+3+4+5=15

Input: N=6
Output: 21
Explanation: 1+2+3+4+5+6=15


Platform:
DSA Sheet

Topic:
Parameterized Recursion

Difficulty:
medium

Approach:
Recursive approach
keep the base condition such that we go from n to 0
 print the total inside the condition
 :return
again in recrusive function reduce the n by 1 and add the n to the total
also :
### Algorithm: Sum of N Numbers Using Recursion

1. Start with `n` and `t = 0`.
2. Check if `n < 0`.
   - If yes, **return/print `t`**.
3. Otherwise:
   - Add `n` to `t`.
   - Decrease `n` by `1`.
   - Recursively call the function with updated `n` and `t`.
4. Repeat until `n < 0`.
5. The final `t` is the **sum of numbers from `n` to 0**.

**Example:** `n = 6` → `6 + 5 + 4 + 3 + 2 + 1 + 0 = 21`

Time Complexity: O(N), as we iterate from 1 to N performing constant-time operation for each iteration.
Space Complexity : O(N), as stack is used
Date Solved:
-14-SEP-2026

Mistake:
add the total while calling the function not before it
Key Takeaway:
print or return the value in base condition
add the total while calling the function not before it



"""


class Solution:

    def solve(self, n,t):
        if n <0:
            print(t)
            return
        self.solve(n-1,t+n)



if __name__ == "__main__":
    solution = Solution()

    # Test your solution
    inp = 6
    total= 0
    result = solution.solve(inp,total)
    print(result)

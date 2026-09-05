"""
Problem:
Count digits
N=1234
output: count = 4

Platform:
Strivers sheet

Topic:
Counting Digits

Difficulty:
easy

Approach:
- Initialize count to 0
- start a while loop while n > 0
- Increase Count
-  divide by 10 to remove the last digit fraction part by converting it into int
- print count

Time Complexity:
- O(log n) removes one digit per iteration
- ## O(1) for optimal approach using log(n)+1
Space Complexity:
- O(1) we use few variables

Date Solved:
-05-SEP-2026

Mistake:
- forgot to conver new number into int

Key Takeaway:
- initialize and increase count after removing last digit

Revision:
[ ] Rev 1
[ ] Rev 2
[ ] Rev 3
"""

import math
class Solution:

    def solve(self,n):
            count = int(math.log10(n)+1)
            # while n>0:
            #
            #     count +=1
            #     n=int(n/10)

            print(f"Count : {count}")


if __name__ == "__main__":
    solution = Solution()

    # Test your solution
    inp=1234
    solution.solve(inp)

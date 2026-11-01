
"""
Problem:
Reverse an Array Using Recursion and Two Pointers

Example 1:
Input : nums = [1, 2, 3, 4, 5]
Output : [5, 4, 3, 2, 1]
Example 2:
Input : nums = [1, 3, 3, 3, 5]
Output : [5, 3, 3, 3, 1]

Platform:
DSA Sheet

Topic:
Parameterized Recursion

Difficulty:
medium

Approach:
Use two Pointers, l and r, starting from the first elements. Swap arr[i] and arr[r],then
recursively move the pointers inward using l+1 and r-1. Stop when the two pointers meet or cross.


Time Complexity: O(N), as each element is visited at most once during the recursive swaps.
Space Complexity : O(N), due to the recursion call stack. The array is modified in-place, so it requires O(1) auxiliary space apart from recursion

Date Solved:
-28-SEP-2026

Mistake:
Initially used the wrong base condition( l <=r), which caused the recursion to stop before performing the requied swaps. The stopping condition should be when the pointers meet or cross.

Key Takeaway:
In two pointer recursion, swap the elements at the current pointers. then move both the pointers towards the center. the base conditon should stop th recursion when l >=r.


"""


class Solution:

    def solve(self, arr, l, r):
        if l >= r:
            return
        arr[l], arr[r] = arr[r], arr[l]
        self.solve(arr, l + 1, r - 1)


if __name__ == "__main__":
    solution = Solution()

    # Test your solution

    array = list(map(int, input("Enter the numbers for the array to sap spearted by ',' : ").split(",")))
    left = 0
    right = len(array) - 1
    solution.solve(array, left, right)
    print(array)

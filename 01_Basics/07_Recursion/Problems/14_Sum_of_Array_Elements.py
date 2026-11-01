"""
Problem:

Sum of Array Elements II

Given an array nums, find the sum of elements of array using recursion.

Example 1:
Input : nums = [1, 2, 3]
Output : 6

Explanation : The sum of elements of array is 1 + 2 + 3 => 6.

Example 2:
Input : nums = [5, 8, 1]
Output : 14
Explanation : The sum of elements of array is 5 + 8 + 1 => 14

Platform:
DSA Sheet

Topic:
Recursion --> array --> Sum of elements

Difficulty:
Easy

Approach:
- Start from index i =0
- if i==n, return 0 because all elements have been processed.
- add the current element arr[i] to the result of recursively processing the remaining array.
- move to the next index using i+1
- continue until the end of the array is reached

Time Complexity:
- O(n) each array element is visited once

Space Complexity:
- O(n) -> Recursion stack contain up to n calls.

Date Solved:
- 1 oct 2026

Mistake:
-when making the recursive call make sure that it has the same arguments as they are while defining that function

Key Takeaway:
- sum = current element+ sum of remaining elements.
-Base case: when i ==n, return 0.

"""


class Solution:

    def solve(self,i,arr):
        n=len(arr)
        if i ==n:
            return 0
        return arr[i]+self.solve(i+1,arr)


if __name__ == "__main__":
    solution = Solution()

    # Test your solution here
    nums=list(map(int,input("Enter numbers separated by a ',' : ").split(",")))
    print(solution.solve(0,nums))
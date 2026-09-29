"""
Problem:
Given an array nums of n integers, return reverse of the array.

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
Start form index i =0
Swap arr[i] with arr[n-i-1]
Recursively move to the next index i+1
stop when i > n//2
This reverses the array in place

Time Complexity: O(N), as each element is visited at most once during the recursive swaps.
Space Complexity : O(N), due to the recursion call stack. The array is modified in-place, so it requires O(1) auxiliary space apart from recursion

Date Solved:
-29-SEP-2026

Mistake: --
Key Takeaway:
last element can be traced for reversing by n-i-1,Swap the first and last elements, then move inward recursively.


"""


class Solution:

    def solve(self, arr,i):
        n = len(arr)
        if i > n//2:
            return
        arr[i],arr[n-i-1] = arr[n-i-1], arr [i]
        self.solve(arr,i+1)



if __name__ == "__main__":
    solution = Solution()

    # Test your solution

    array=list(map(int,input("Enter the numbers for the array to sap spearted by ',' : ").split(",")))
    left = 0
    right =len(array)-1
    solution.solve(array, 0)
    print(array)


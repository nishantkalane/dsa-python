"""
Problem:
Check if the Array is Sorted II
We need to determine whether an array is sorted in non-decreasing order.
That means every element must be less than or equal to the next element.
For example:
[1, 2, 3, 4, 5]  → true
[1, 2, 1, 4, 5]  → false
[1, 2, 2, 4, 4]  → true
Notice that equal values are allowed.

Platform:
DSA Sheet

Topic:
Recursion -> Array -> Sorted Check

Difficulty:
Easy

Approach:
- Start from index i =0.
- Compare the current element arr[i] with eht next element arr[i+1]
-if arr[i] > arr[i+1], the array is not sorted so return False.
- Otherwise, recursively check the next pair using i+1
-When i reaches the last element all pairs have been checked so return True.

Time Complexity:
- O(n) - Each adjacent pair is checked once.

Space Complexity:
- O(n) - Recursion Stack

Date Solved:
- 02 oct 2026

Mistake:
-arr[i] > arr[i+1] correctly allows equal values.

Key Takeaway:
- for non-decreasing order, only return False when arr[i] > arr[i+1]; equal values are allowed.


"""


class Solution:

    def solve(self,i,arr):
        n =len(arr)
        if i ==n-1:
            return True
        if arr[i] > arr[i+1]:
            return False
        return self.solve(i+1,arr)


if __name__ == "__main__":
    solution = Solution()

    # Test your solution here
    array = list(map(int,input("Enter the numbers seprated by ',': ").split(',')))
    print(solution.solve(0,array))
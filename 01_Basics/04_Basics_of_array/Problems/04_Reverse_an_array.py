"""
Problem:
Reverse an Array

Input:
arr = [1, 2, 3, 4, 5]

Output:
arr = [5, 4, 3, 2, 1]

Platform:
Sheet

Topic:
Basic Arrays / Two Pointers / Swapping

Difficulty:
easy

Approach:
- Initialize left = 0
- Initialize right = len(arr) - 1
- Start a while loop while left < right
- Swap arr[left] and arr[right]
- Increment left by 1
- Decrement right by 1
- Repeat until both pointers meet or cross
- Return the reversed array

Time Complexity:
- O(n), approximately n/2 swaps

Space Complexity:
- O(1), reverses the original array in-place

Date Solved:
- 01-NOV-2026

Mistake:
- The condition in while loop was done wrong instead of l < r, I wrote l>r

Key Takeaway:
- Use two pointers from opposite ends and swap elements to reverse an array in-place.
"""

class Solution():
    def solve(self, array, l, r):

        while l < r:
            array[l],array[r] = array[r],array[l]
            l +=1
            r -=1

        return array


if __name__ == "__main__":
    sol = Solution()

    arr = list(map(int,input("Enter and array separated by a ',' ").split(',')))
    left = 0
    right = len(arr)-1
    print(sol.solve(arr,left,right))
    print(arr)
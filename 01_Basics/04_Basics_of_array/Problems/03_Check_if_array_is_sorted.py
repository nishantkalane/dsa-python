

"""
Problem:
Check if the Array is Sorted I

Input:
arr = [1, 2, 2, 3, 4]

Output:
True

Platform:
Sheet

Topic:
Basic Arrays / Array Traversal / Adjacent Comparison

Difficulty:
easy

Approach:
- Traverse the array from index 0 to n-2
- Compare the current element with the next element
- Check if arr[i] > arr[i+1]
- If true, return False immediately
- If no violation is found, return True
- Equal elements are allowed because the array is in non-decreasing order

Time Complexity:
- O(n), worst case when all elements are checked
- O(1), best case when the first comparison fails

Space Complexity:
- O(1), uses no extra data structure

Date Solved:
- 01-NOV-2026

Mistake:
- ---
Key Takeaway:
- Compare adjacent elements to check whether an array is sorted in non-decreasing order.
"""

class Solution():
    def solve(self,array):
        for i in range(len(array)):
            if array[i] > array[i+1]:
                return False
            else:
                return True



if __name__ == "__main__":
    sol = Solution()

    arr = list(map(int,input("Enter and array separated by a ',' ").split(',')))
    print(sol.solve(arr))
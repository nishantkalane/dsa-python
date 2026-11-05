"""
Problem:
Sort the given array in ascending order using Bubble Sort.

Example: arr = [64, 34, 25, 12, 22, 11, 90]
Output: [11, 12, 22, 25, 34, 64, 90]

Platform:
Striver's Sheet / DSA Practice

Topic:
Sorting Algorithms

Pattern:
Adjacent Comparison / Swapping

Difficulty:
Easy

Approach:
- Initialize the outer loop for n-1 passes.
- Initialize did_swap = 0 at the beginning of every pass.
- Traverse the unsorted portion using j = 0 to n-2-i.
- Compare adjacent elements arr[j] and arr[j+1].
- If arr[j] > arr[j+1], swap both elements and set did_swap = 1.
- After completing each pass, check did_swap.
- If did_swap == 0, break because the array is already sorted.
- Repeat until the array is sorted.

Time Complexity:
- Best Case: O(n) with the swapped flag optimization.
- Average Case: O(n²).
- Worst Case: O(n²).

Space Complexity:
- O(1), in-place sorting.

Date Solved: 5 Nov 2026

Mistake:
- Initially initialized did_swap = 0 inside the inner loop instead of before it.
- Checked did_swap before completing the entire pass instead of after the inner loop.

Key Takeaway:
- Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order. The largest unsorted element moves to the end after every pass.
"""
class Sort:
    def bubble_sort(self,arr):
        n = len(arr)
        for i in range(n-1):
            did_swap = 0
            for j in range(n-1-i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    did_swap += 1
                if did_swap == 0:
                    break
if __name__ ==  "__main__":
    sol = Sort()

    array = list(map(int,input("Enter numbers to sort by bubble sort (enter numbers separated  by ',': ").split(",")))

    sol.bubble_sort(array)
    print(array)
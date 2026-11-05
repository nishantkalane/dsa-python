"""
Problem:

Sort the given array in ascending order using Insertion Sort.

Example: arr = [12, 11, 13, 5, 6]
Output: [5, 6, 11, 12, 13]

Platform:
Striver's Sheet / DSA Practice

Topic:
Sorting Algorithms

Pattern:
Insertion / Adjacent Comparison / Swapping

Difficulty:
Easy

Approach:
- Traverse the array from index i = 0 to n-1.
- Initialize j = i to track the current element's position.
- Compare the current element arr[j] with its previous element arr[j-1].
- If arr[j-1] > arr[j], swap the adjacent elements.
- Decrement j to move towards the beginning of the array.
- Continue until j = 0 or the previous element is smaller or equal.
- Repeat for every element until the array is sorted.

Time Complexity:
- Best Case: O(n), when the array is already sorted.
- Average Case: O(n²).
- Worst Case: O(n²), when the array is reverse sorted.

Space Complexity:
- O(1), in-place sorting without using an extra array.

Date Solved: 5 Nov 2026

Mistake:
- Initially needed clarification about the difference between shifting and adjacent swapping approaches.
- The condition j > 0 prevents accessing an invalid previous position during comparisons.
-the inversion of grater than in and led to descending order

Key Takeaway:
- Insertion Sort builds a sorted portion from left to right.
- Each element moves left through adjacent swaps until it reaches its correct position.
- Adjacent swapping is an alternative implementation of Insertion Sort, while shifting is generally more efficient in terms of assignments.

"""
class Sort:
    def insertion_sort(self,arr):
        n = len(arr)
        for i in range(n):
            j =i
            while j > 0 and arr[j-1] > arr[j]:
                arr[j-1],arr[j] = arr[j], arr[j-1]
                j -=1




if __name__ == "__main__":
    sol = Sort()

    array = list(map(int,input("Enter numbers to sort by selection sort (enter numbers separated  by ',': ").split(",")))
    sol.insertion_sort(array)
    print(array)
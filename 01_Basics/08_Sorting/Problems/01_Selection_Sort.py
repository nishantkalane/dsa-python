
"""
Sort the given array in ascending order using Selection Sort.

Example: arr = [64, 25, 12, 22, 11]
Output: [11, 12, 22, 25, 64]

Platform:
Striver's Sheet / DSA Practice

Topic:
Sorting_algorithms

Pattern:
Selection of Minimum/ Swapping

Difficulty:
Easy

Approach:
- Initialize the outer loop from i =0 to n-2 ( in range(n-1))
- Assume the current index i contains the minimum element ( mini =i)
- Traverse the remaining unsorted portion using j = i+1 to n-1.
- If arr[j] is smaller than arr[mini], update mini = j.
- After finding the minimum element, swap arr[mini] with arr[i].
- Repeat until the array is sorted.

Time Complexity:
- O(n2)

Space Complexity:
- O(1), n place sorting

Date Solved:
- 5 Nov 2026

Mistake:
- initially used range(n-1) for the inner loop instead of range(i+1,n)
- used range(n-2) for the outer loop instead of range(n-1)


Key Takeaway:
- Selection Sort repeatedly finds the minimum element from the unsorted portion and places t at the
beginning.

"""
class Sort:
    def seclection_sort(self,arr):
        n=len(arr)
        for i in range(n-1):
            mini = i
            for j in range(i+1,n):
                if arr[j] < arr [mini]:
                    mini = j
            arr[mini], arr[i] = arr [i], arr[mini]

if __name__ == "__main__":
    sol = Sort()

    array = list(map(int,input("Enter numbers to sort by selection sort (enter numbers separated  by ',': ").split(",")))
    sol.seclection_sort(array)
    print(array)

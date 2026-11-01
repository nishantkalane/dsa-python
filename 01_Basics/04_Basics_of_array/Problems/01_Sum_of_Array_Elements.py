"""
Problem:
Sum of Array Elements

Input:
arr = [1, 2, 3, 4, 5]

Output:
sum = 15

Platform:
Sheet

Topic:
Basic Arrays / Array Traversal / Accumulator

Difficulty:
easy

Approach:
- Initialize sum = 0
- Traverse the array using a for loop
- Add each element to sum
- Return the final sum

Time Complexity:
- O(n), traverse all n elements once

Space Complexity:
- O(1), uses only one extra variable

Date Solved:
- 01-NOV-2026

Mistake:
- -

Key Takeaway:
- Use an accumulator variable to maintain a running sum of array elements.

"""



class Solution:
    def solve(self,array):
        total = 0
        # by index :
        for i in range(len(array)):
            total += array[i]
        print(total)

        # #by direct access
        # for r in array:
        #     total +=r
        # print(total)


if __name__ == "__main__":
    sol = Solution()

    arr = list(map(int,input("Enter and array separated by a ',' ").split(',')))
    sol.solve(arr)

#TC= O(n)
#SC = O(1)
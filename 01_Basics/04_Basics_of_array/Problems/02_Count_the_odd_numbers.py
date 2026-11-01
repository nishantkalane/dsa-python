"""
Problem:
Count of Odd Numbers in Array

Input:
arr = [1, 2, 3, 4, 5, 7]

Output:
count = 4

Platform:
Sheet

Topic:
Basic Arrays / Counting / Modulo Operator

Difficulty:
easy

Approach:
- Initialize count = 0
- Traverse the array using a for loop
- Check if arr[i] % 2 != 0
- If true, increment count by 1
- Return the final count

Time Complexity:
- O(n), checks every element once

Space Complexity:
- O(1), uses only one counter variable

Date Solved:
- 01-NOV-2026

Mistake:
- --

Key Takeaway:
- Use the modulo operator (% 2) to identify odd and even numbers.

"""
class Solution():
    def solve(self,array):
        count = 0
        for num in array:
            if num % 2 !=0:
                count +=1
        print(count)

if __name__ == "__main__":
    sol = Solution()

    arr = list(map(int,input("Enter and array separated by a ',' ").split(',')))
    sol.solve(arr)



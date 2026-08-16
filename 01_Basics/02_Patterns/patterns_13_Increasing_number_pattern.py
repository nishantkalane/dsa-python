"""
Problem:
- Given and Integer N, Print the following Pattern:
 1
 2 3
 4 5 6
 7 8 9 10

Platform: Strivers sheet

Topic:
-Flyod's Triangle

Difficulty:
-Medium

Approach:
- This pattern prints a continuous sequence of increasing numbers, arranged row by row in a triangular structure. Each row has more number than the previous,
and the values increment consecutively throughout the triangle.

-Intitalize a variable to 1, keep it outside as we do not want to reset the value any other in starting of each row
-loop through 1 to n to handel each row
-for each row , print i numbers starting from the current value of the number variable
-increment the number after each print to maintain the continuous sequence
-After prining all the number in a row, move to the next line.

Time Complexity:
- O(N^2)

Space Complexity:
- O(1)

Date Solved:
- 16-Aug-2026

Key Takeaway:
- keep the variable outside the loops to have a number initialized once and then increment or decrement inside
inner loop to have a certain patern throughout the pattern

Revision:
[ ] Rev 1
[ ] Rev 2
[ ] Rev 3
"""


class Solution:

    def solve(self,n):
        p=1
        for i in range(n):
            for j in range(i+1):

                print(p, end=" ")
                p += 1

            print()


if __name__ == "__main__":
    solution = Solution()

    # Test your solution here
    n=5
    solution.solve(n)
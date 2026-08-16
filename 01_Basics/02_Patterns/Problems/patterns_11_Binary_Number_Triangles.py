"""
Problem:
    Binary Number Triangle
    Given an integer N, print the following pattern :
    1
    0 1
    1 0 1
    0 1 0 1
    1 0 1 0 1


Platform:
    Striver's

Topic:

Difficulty:
    Hard

Approach:
- This pattern prints alternating 1s and 0s in each row, starting with 1 on even-Indexed rows and 0 on odd-Indexed rows. The vlaue alternates after each print using basic toggling logic

- Take N as input
-Loop from 0 to N
- Have condtionals to change initialization of each row after the outer loop
-Print the varialbe
- Inside inner loop use math function k=1-k or the behaviour that sum of row and column indices is even print  1 else 0, use logics


Time Complexity:
O(N^2)

Space Complexity:
O(1)
Date Solved:
26/08/2026

Mistake:
-
Didn't know that if we need to initialize row state we can do it just below the outer for loop

Key Takeaway:
-
If we need to initialize new point every row we do it just next to outer loop start
Flipping a variable between 0 and 1 can be done by changing the variable inside the inner loop by math shortcut of k= 1-k

Revision:
[ ] Rev 1
[ ] Rev 2
[ ] Rev 3
"""




class Solution:

    def pattern_11(self,n):
        for i in range(n):
            if(i%2==0) :
                k=1
            else:
                k=0
            for j in range(i+1):
                print(k,end=" ")
                k = 1 - k

            print()


if __name__ == "__main__":
    solution = Solution()
    n=5
    solution.pattern_11(n)


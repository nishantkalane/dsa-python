"""
Problem:
Generate all possible subsets (subsequences) of an array using recursion by making a take / not-take decision for every element.

Platform:
DSA Sheet

Topic:
Recursion - Printing Subsequences


Difficulty:
Hard

Approach:
- Start from index i =0  with an empty list ls.
- For the current element arr[i], make two choices
--Take: Add arr[i] to ls and recursively process the next element.
--Not Take: Remove the last added element using pop() and recursively process the next element.
-Continue making these two choices for every element.
-when i >=n, all elements have been considered, so print the current ls.
-This generates every possible subset, including the empty subset.

Time Complexity:
- O(n * 2^n) -> 2^n subsets are generated, and printing each subset can take up to O(n).

Space Complexity:
- O(n) -> recursion stack + current subset ls.

Date Solved:
- 30-Sep-2026

Mistake:
- ls.pop() is correct because it removes the last element that was added before exploring the not-take branch.

Key Takeaway:
- Every element has two choices: Take or Not Take -- 2^n possible subsets.

"""


class Solution:

    def solve(self,i,arr,ls):
        n=len(arr)
        #print
        if(i >=n):
            print(ls)
            return
        #take
        ls.append(arr[i])
        self.solve(i+1,arr,ls)

        #remove
        ls.pop()
        self.solve(i+1,arr,ls)



if __name__ == "__main__":
    solution = Solution()

    # Test your solution here
    array=list(map(int,input("Enter array with ',' between numbers: ").split(",")))
    listt=[]
    solution.solve(0,array,listt)
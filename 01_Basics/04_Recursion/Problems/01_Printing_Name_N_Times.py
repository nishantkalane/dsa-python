"""
Problem:
Print from 1 to N using recursion
input=3
input=nish
output :
nish
nish
nish

Platform:
Striver A to Z sheet

Topic:
Recursion

Type:
Basic recursion

Difficulty:
easy

Approach:
-To print your name N times using recursion,
the approach involves defining a recursive function that takes the current count as a parameter.
The function checks if the count has reached N, if it has, the recursion terminates. Otherwise,
it prints the name once and recursively calls itself, incrementing the count by one.
This way, the name gets printed exactly N times as the recursion progresses.
The key is to use the count to keep track of how many times the name has been printed so far and stop once it reaches N.

Time Complexity: O(N), we print our name exactly N times.

Space Complexity: O(N), stack space used for recursive calls.

Date Solved:
- 9-Sep-2026

Mistake:
- Didn't pass the arguments correctly

Key Takeaway:
- Give the parameters to loop correctly and you can declare i while calling it and then reuse it with a condition for creating a base condition

"""

class Solution:
    def solve(self,name,i,n):

        if i ==n:
            return
        print(name)
        self.solve(name,i+1,n)




if __name__ == "__main__":
    solution = Solution()

    # Test your solution here
    inp = int(input("How many times you want to print your name?"))
    print_name= input("What's your name?")
    solution.solve(print_name,0,inp)



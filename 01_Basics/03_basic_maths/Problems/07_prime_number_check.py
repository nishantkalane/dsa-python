"""
Problem:
Check weather a number is prime or not
N= 7
output: True
M=6
output: False

Platform:
Strivers sheet

Topic:
Prime number check

Difficulty:
medium

Approach:
Linear method:
    loop in range form 1 to n+1
    check if diving n by i results in 0 append 1 to counter
    print counter is equal to 2 print true else false

optimal square root method:
    use while loop to check the square root is less than n  that is loop till eg 6*6 is less than 36
    then check if n is divisible by i if yes increase counter by
    in the indented if condition check now if n/i is not equal to i so that i doesn't come twice thus we get the another side of the multiples, if yes increment cnt by 1
    increment i
    return true if cnt == 2 else false

Linear Method:
Time Complexity: O(N), as we iterate from 1 to N performing constant-time operation for each iteration.
Space Complexity : O(1), as the space used by the algorithm does not increase with the size of the input..

Optimal Method:
Time Complexity: O(sqrt(N)), as The loop iterates up to the square root of n performing constant time operations at each step.
Space Complexity : O(1), as the space complexity remains constant and independent of the input size. Only a fixed amount of memory is required to store the integer variables.

Date Solved:
-07-SEP-2026

Mistake:
-in optimal apporach forgot to ran while loop less than equal to n
Key Takeaway:
- In optimal approach run the while loop for less than equal to n


"""


class Solution:

    def solve(self, n):
        # Linear method :
        # cnt = 0
        # for i in range(1,n+1):
        #     if n % i ==0:
        #         cnt +=1
        # if cnt == 2:
        #     return True
        # else:
        #     return False

        #optimal method
        i=1
        cnt=0
        while i*i<=n:
            if n %i ==0:
                cnt +=1
                if n//i !=i:
                    cnt+=1
            i +=1
        if cnt == 2:
            return True
        else:
            return False




if __name__ == "__main__":
    solution = Solution()

    # Test your solution
    inp = 6
    result = solution.solve(inp)
    print(result)

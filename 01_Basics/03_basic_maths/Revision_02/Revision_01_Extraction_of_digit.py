
class Solution:
    def solve(self,n):
        while n > 0:
            last_digit= n %10
            print(last_digit)
            n = n //10


if __name__ == "__main__" :
    sol = Solution()

    inp =12345
    sol.solve(inp)

# TC : O(log10(N)+1), where n is the input number, in the while loop we divide N by 10 until it becomes 0 which takes 1og10N iterations
 # i.e we perform division in loop
# SC : O(1), as only a constant amount of additional memory for the counter regardless of size of the input number.


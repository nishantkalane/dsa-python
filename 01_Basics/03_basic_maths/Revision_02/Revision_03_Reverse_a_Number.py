
class Solution:
    def solve(self,n):
        res =[]
        while n > 0:
            last_digit= n %10
            # res.append(last_digit)
            print(last_digit)
            n = n //10
        return res


if __name__ == "__main__" :
    sol = Solution()

    inp =12345
    result=sol.solve(inp)
    print(*result)

# TC : O(log10(N)+1), where n is the input number, in the while loop we divide N by 10 until it becomes 0 which takes 1og10N iterations
 # that is we perform division in loop
# SC : O(1),Only a constant number of variables are used regardless of the size of the input number.


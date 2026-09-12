import math
class Solution:
    def solve(self,n):
        # cnt =0
        # while n > 0:
        #     cnt +=1
        #     n = n //10
        # return cnt
        cnt = int(math.log10(n)+1)
        return cnt

if __name__ == "__main__" :
    sol = Solution()

    inp =642
    result=sol.solve(inp)
    print(result)

# TC : O(log10(N)+1), where n is the input number, in the while loop we divide N by 10 until it becomes 0 which takes 1og10N iterations
 # i.e we perform division in loop
# SC : O(1), as only a constant amount of additional memory for the counter regardless of size of the input number.

#Math way :

#TC : O(1),   as simple arithmetic operations in constant time are computed on integers
#SC : O(1), as only a constant amount of additional memory for the count variable regardless of size of the input number.

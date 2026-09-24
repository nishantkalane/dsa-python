
class Solution:
    def solve(self, n):

        # #method 1:
        # cnt=0
        #
        # for i in range(1, n+1):
        #     if n % i==0:
        #         cnt +=1
        # if cnt ==2:
        #     return True
        # else:
        #     return False
        #Method 2:
        i=1
        cnt =1
        while i*i<n:
            if n % i ==0:
                cnt+=1
                if n // i !=i:
                    cnt+=1
            i +=1
        if cnt ==2:
            return True
        else:
            return False

# =====================================================================
# COMPLEXITY ANALYSIS COMPARISON:
# =====================================================================
# Method 1: Time: O(n)       | Space: O(1) -> Linear scan; checks all factors.
# Method 2: Time: O(sqrt(n)) | Space: O(1) -> Most efficient correct choice.
# =====================================================================




if __name__ == "__main__":
    sol = Solution()

    inp1=int(input())
    result=sol.solve(inp1)
    print(result)
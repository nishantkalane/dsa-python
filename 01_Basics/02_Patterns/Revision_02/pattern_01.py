class Solution:
    def pattern_01(self,n):
        for i in range(n):
            for j in range(n):
                print("*",end=" ")
            print()

if __name__ == "__main__" :
    sol = Solution()
    n=12
    sol.pattern_01(n)
class Solution:
    def pattern_10(self,n):
        for i in range(n-1):
            for j in range(i+1):
                print("*", end=" ")
            print()
        for i in range(n):
            for j in range(i, n):
                print("*", end=" ")
            print()
if __name__ == "__main__" :
    sol=Solution()
    n=7
    sol.pattern_10(n)
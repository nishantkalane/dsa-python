class Solution:
    def pattern_05(self,n):
        for i in range(n):
            for j in range(i,n):
                print("*", end = " ")
            print()

if __name__ == "__main__" :
    sol=Solution()
    n=7
    sol.pattern_05(n)
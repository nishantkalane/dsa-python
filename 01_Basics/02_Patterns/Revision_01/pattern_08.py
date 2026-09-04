class Solution:
    def pattern_08(self,n):
        for i in range(n):
            for j in range(i+1):
                print(" ", end=" ")
            for j in range(i,n-1):
                print("*", end=" ")
            for j in range(i,n):
                print("*", end=" ")
            print()

if __name__ == "__main__" :
    sol=Solution()
    n=7
    sol.pattern_08(n)
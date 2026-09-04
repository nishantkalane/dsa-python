class Solution:
    def pattern_19(self,n):
        for i in range(n-1):
            for j in range(i,n):
                print("*",end="")
            for j in range(i):
                print(" ",end="")
            for j in range(i):
                print(" ",end="")
            for j in range(i,n):
                print("*", end="")
            print()
        for i in range(n):
            for j in range(i + 1):
                print("*", end="")
            for j in range(i, n - 1):
                print(" ", end="")
            for j in range(i, n - 1):
                print(" ", end="")
            for j in range(i + 1):
                print("*", end="")
            print()




if __name__ == "__main__" :
    sol=Solution()

    n=5
    sol.pattern_19(n)
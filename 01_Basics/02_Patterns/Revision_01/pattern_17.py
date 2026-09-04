class Solution:
    def pattern_17(self, n):
        for i in range(n):
            p = ord("A")
            for j in range(i,n):
                print(" ", end="")
            for j in range(i):
                print(chr(p),end="")
                p+=1
            for j in range(i+1):
                print(chr(p), end="")
                p-=1
            print()



if __name__ == "__main__":
    sol = Solution()
    n=5
    sol.pattern_17(n)

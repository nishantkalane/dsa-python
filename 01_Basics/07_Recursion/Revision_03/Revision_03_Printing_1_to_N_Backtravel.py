class Solution:
    def solve(self,n,i):
        if i == 0:
            return
        self.solve(n,i-1)
        print(i)

if __name__ == "__main__":
    sol = Solution()

    inp=int(input("Enter tor print 1 to N back travel : "))
    sol.solve(inp,inp)
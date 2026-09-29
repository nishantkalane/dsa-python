class Solution:
    def solve(self,n,summ):
       if n <0:
           return
       self.solve(n-1,summ+n)

if __name__ == "__main__":
    sol = Solution()
    inp = 3
    sumt =0
    r=sol.solve(inp,sumt)


# TC = O(N)
# SC= O(N)
class Solution:
    def solve(self,n,total):
         if n == 0:
             return total
         self.solve(n-1,total= total+n)
    #
if __name__  == "__main__":
    sol = Solution()

    inp = int(input())
    tot = 0
    sol.solve(inp,tot)
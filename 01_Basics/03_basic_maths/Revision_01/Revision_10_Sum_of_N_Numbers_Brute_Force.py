class Solution:
    def solve(self, n):
       summ=0
       for i in range(1,n+1):
           summ +=i
       print(summ)


if __name__ == "__main__":
    sol = Solution()
    inp = 2
    sol.solve(inp)

# TC = O(N)
# SC= O(1)
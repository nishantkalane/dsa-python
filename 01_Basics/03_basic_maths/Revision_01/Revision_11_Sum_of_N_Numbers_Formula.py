class Solution:
    def solve(self, n):
       return (n*(n+1))//2



if __name__ == "__main__":
    sol = Solution()
    inp = 2
    r=sol.solve(inp)
    print(r)
# TC = O(N)
# SC= O(1)
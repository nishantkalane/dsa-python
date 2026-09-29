class Solution:
    def solve(self, n):
        if n ==0:
            return 1
        return n*(self.solve(n-1))



if __name__ == "__main__":
    sol = Solution()
    inp = 6
    r= sol.solve(inp)
    print(r)
# TC = O(N)
# SC= O(N)
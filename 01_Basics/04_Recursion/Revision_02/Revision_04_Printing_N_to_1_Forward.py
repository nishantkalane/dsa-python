class Solution:
    def solve(self,i, n):
        if n <1:
            return
        print(i)
        self.solve(i-1,n-1)


if __name__ == "__main__":
    sol = Solution()
    inp = 5
    sol.solve(inp,inp)

# TC = O(N)
# SC= O(N)
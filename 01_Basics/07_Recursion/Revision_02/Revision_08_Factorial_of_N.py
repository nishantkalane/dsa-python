class Solution:
    def solve(self,n):
        if n == 1:
            return 1
        return n*self.solve(n-1)


if __name__ == "__main__" :
    sol = Solution()
    inp=int(input("Enter n to get it's factorial: "))
    print(sol.solve(inp))



# TC= O(N))
# SC= O(N)
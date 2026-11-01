class Solution:
    def solve(self,i, n):
        if i ==0 :
            return
        self.solve(i-1,n)
        print(i)



if __name__ == "__main__":
    sol = Solution()
    inp = 6
    sol.solve(inp,inp)

# TC = O(N)
# SC= O(N)
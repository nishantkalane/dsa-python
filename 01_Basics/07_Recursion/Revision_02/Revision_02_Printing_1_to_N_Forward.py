class Solution:
    def solve(self,i, n):
        if i > n:
            return
        print(i)
        self.solve(i+1,n)


if __name__ == "__main__":
    sol = Solution()
    inp = 5
    sol.solve(1,inp)

# TC = O(N)
# SC= O(N)
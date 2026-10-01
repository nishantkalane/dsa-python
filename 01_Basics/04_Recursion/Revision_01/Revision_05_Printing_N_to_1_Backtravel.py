class Solution:
    def solve(self,i, n):
       if i >n:
           return
       self.solve(i+1,n)
       print(i)
if __name__ == "__main__":
    sol = Solution()
    inp = 5
    sol.solve(1,inp)

# TC = O(N)
# SC= O(N)
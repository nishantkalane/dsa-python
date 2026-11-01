class Solution:
    def solve(self,n):
        if n ==0:
            return n
        return n+self.solve((n-1))

if __name__ == "__main__" :
    sol= Solution()

    inp= int(input("Enter n: "))

    print(sol.solve(inp))
# TC= O(log(n))
# SC= O(1)
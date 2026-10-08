class Solution:
    def solve(self, n, m):
       for i in range(m):
           for j in range(m):
               print(n-min(i,j,m-i-1,m-j-1),end=" ")
           print()


if __name__ == "__main__":
    sol = Solution()

    inp = int(input("enter n: "))
    inm = (inp*2)-1
    sol.solve(inp,inm)


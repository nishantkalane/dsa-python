class Solution:
    def solve(self, n):
        for i in range(n):
            for j in range(n):
                if  j ==0 or i ==n-1 or i==0 or j ==n-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")


            print()

if __name__ == "__main__":
    sol = Solution()

    inp =int(input("enter n: "))
    sol.solve(inp)


class Solution:
    def solve(self, n):
        for i in range(n-1):
            for j in range(i,n):
                print("*",end=" ")
            for j in range(i):
                print(" ", end=" ")
            for j in range(i):
                print(" ",end=" ")
            for j in range(i,n):
                print("*", end=" ")
            print()
        for i in range(n):
            for j in range(i+1):
                print("*",end=" ")
            for j in range(i,n-1):
                print(" ", end=" ")
            for j in range(i,n-1):
                print(" ",end=" ")
            for j in range(i+1):
                print("*", end=" ")
            print()



if __name__ == "__main__":
    sol = Solution()

    n = int(input())
    sol.solve(n)

#TC: O(n^2): due to nested loops executing operations proportional to the square of n.
#SC: O(1): as it uses only a fixed amount of extra memory for loop variables.

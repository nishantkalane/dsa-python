class Solution:
    def solve(self, n):
        for i in range(n-1):
            for j in range(i + 1):
                print("*", end=" ")
            for j in range(i, n - 1):
                print(" ", end=" ")
            for j in range(i, n - 1):
                print(" ", end=" ")
            for j in range(i + 1):
                print("*", end=" ")
            print()
        for i in range(n):
            for j in range(i, n):
                print("*", end=" ")
            for j in range(i):
                print(" ", end=" ")
            for j in range(i):
                print(" ", end=" ")
            for j in range(i, n):
                print("*", end=" ")
            print()



if __name__ == "__main__":
    sol = Solution()

    inp = int(input("enter n: "))
    sol.solve(inp)


#TC : O(n^2) due to nested oops that execute operations proportional to the square of n.
#SC: O(1) because it directly prints the output using a fixed amount of memory for vaiables


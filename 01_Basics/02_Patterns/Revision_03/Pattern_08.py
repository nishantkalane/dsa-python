class Solution():
    def solve(self,n):
        for i in range(n):
            for j in range(i+1):
                print(" ", end="")
            for j in range(i,n-1):
                print("*", end="")
            for j in range(i,n):
                print("*", end="")
            print()


if __name__ == "__main__" :
    sol = Solution()

    n=5
    sol.solve(n)

#tc : O(N2), since nested loops print about N^2 characters overall
#SC : O(1), as no extra data structures are required
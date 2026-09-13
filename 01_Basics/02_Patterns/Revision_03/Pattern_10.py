class Solution():
    def solve(self,n):

        for i in range(n-1):
            for j in range(i+1):
                print("*", end="")
            print()
        for i in range(n):
           for j in range(i,n):
                print("*",end="")
           print()

if __name__ == "__main__" :
    sol = Solution()

    n=5
    sol.solve(n)

#tc : O(N2), because there are nested loops that print a total of N^2 characters

#SC : O(1), as we use only variables and no extra data structures

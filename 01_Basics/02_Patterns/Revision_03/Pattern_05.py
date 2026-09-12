
class Solution:
    def solve(self,n):
        for i in range(n):
            for j in range(n-i):
                print("*",end="")
            print()



if __name__ == "__main__" :
    sol = Solution()

    n =5
    sol.solve(n)

#TC : O(N^2), because there are two nested loops, the outer loop for rows and the inner loop for printing column
#SC : O(1), as no extra data structures are needed

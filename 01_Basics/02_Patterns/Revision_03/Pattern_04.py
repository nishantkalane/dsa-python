
class Solution:
    def solve(self,n):
        p=1
        for i in range(n):
            for j in range(i+1):
                print(p,end="")
            p+=1
            print()


if __name__ == "__main__" :
    sol = Solution()

    n =5
    sol.solve(n)

# TC : O(n^2) because there are two nested loops: the outer loop for rows and the inner loop for printing numbers
# SC : O(1) as only loop variables are used.

class Solution:
    def solve(self,n):
        for i in range(n):
            p=1
            for j in range(i,n):
                print(p,end="")
                p +=1
            print()


if __name__ == "__main__" :
    sol = Solution()

    n =5
    sol.solve(n)

#TC : O(N^2) as two nested loops are used
#SC : O(1) as only one loop variable is used

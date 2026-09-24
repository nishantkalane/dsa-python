class Solution:
    def solve(self, n):
        p=1
        for i in range(n):
            for j in range(i+1):
                print(p,end=" ")
                p +=1
            print()



if __name__ == "__main__":
    sol = Solution()

    n = 4
    sol.solve(n)
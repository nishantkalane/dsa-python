class Solution:
    def solve(self,a,b):

        while b !=0:
            a,b = b, a % b
        return a


if __name__ == "__main__":
    sol = Solution()

    inp1=24
    inp2=36
    print(sol.solve(inp1,inp2))
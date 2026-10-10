class Solution:
    def solve(self,n):
        print((n*(n+1))//2)

if __name__ == "__main__":
    sol=Solution()
    inp = int(input("Enter a number to find out the number of digits in it: "))
    sol.solve(inp)
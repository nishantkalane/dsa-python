class Solution:
    def solve(self,i,n):
        if i<=0:
            return
        print(i)
        sol.solve(i-1,n)

if __name__ == "__main__":
    sol=Solution()

    inp=int(input("Enter a number to print it in backwards : "))
    sol.solve(inp,inp)

#TC = O(n)
#SC = O(n)
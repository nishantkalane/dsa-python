class Solution:
    def solve(self,n,i):
        if i >n:
            return
        print(i)
        self.solve(n,i+1)

if __name__ == "__main__":
    sol=Solution()
    inp = int(input("Enter a number to print number in forward manner in it : "))
    sol.solve(inp,1)

#TC: O(n)
#SC: O(n)
class Solution:
    def solve(self,n):
        count =0
        while n > 0:
            count +=1
            n //=10
        print(count)

if __name__ == "__main__":
    sol=Solution()
    inp = int(input("Enter a number to find out the number of digits in it: "))
    sol.solve(inp)
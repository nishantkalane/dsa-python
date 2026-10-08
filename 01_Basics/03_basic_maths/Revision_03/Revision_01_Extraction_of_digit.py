class Solution:
    def solve(self,n):
        lenn=len(str(n))
        for i in range(lenn):
            last_digit = n % 10
            print(last_digit)
            n //=10

if __name__ == "__main__" :
    sol= Solution()

    inp= int(input("Enter a number to separate it's digit: "))

    sol.solve(inp)

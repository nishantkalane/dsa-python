class Solution:
    def solve(self,n):
        max_digit=0
        while n > 0:
            last_digit= n % 10
            if last_digit > max_digit:
                max_digit = last_digit
            #removing the last digit

            n //=10
        print(max_digit)

if __name__ == "__main__":
    sol=Solution()
    inp = int(input("Enter a number to get the largest digit in it: "))
    sol.solve(inp)
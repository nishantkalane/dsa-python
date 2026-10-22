class Solution:
    def solve(self,n):
        dup= n
        divisor_addition =0
        i=1
        while i*i <= n:
            if n % i == 0:
                divisor_addition += i
                if n//i and n*i !=n:
                    divisor_addition += n//i
            i+=1
        if dup == divisor_addition:

            print("It's a perfect number")
        else:
            print("It's not a perfect number")

if __name__ == "__main__":
    sol = Solution()

    inp= int(input("Enter a number to check weather it's a perfect number or not: "))
    sol.solve(inp)
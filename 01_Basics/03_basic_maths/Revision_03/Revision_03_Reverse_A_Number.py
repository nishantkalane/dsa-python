class Solution:
    def solve(self,n):
        rev_no = 0
        while n > 0:
            last_digit = n %10
            rev_no = rev_no * 10
            rev_no +=last_digit
            n //=10
        print(rev_no)

if __name__ == "__main__" :
    sol= Solution()

    inp= int(input("Enter a number to separate it's digit: "))

    sol.solve(inp)
# TC= O(log(n))
# SC= O(1)

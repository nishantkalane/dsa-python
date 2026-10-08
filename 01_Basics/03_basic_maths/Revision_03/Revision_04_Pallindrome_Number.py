class Solution:
    def solve(self,n):
        dup =n
        rev_no = 0
        while n > 0:
            last_digit = n %10
            rev_no = rev_no * 10
            rev_no +=last_digit
            n //=10
        if rev_no == dup:
            return True
        else:
            return False

if __name__ == "__main__" :
    sol= Solution()

    inp= int(input("Enter to check a palindrome: "))

    r=sol.solve(inp)
    print(r)
# TC= O(log(n))
# SC= O(1)
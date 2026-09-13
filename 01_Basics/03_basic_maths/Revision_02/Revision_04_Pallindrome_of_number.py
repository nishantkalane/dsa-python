class Solution:
    def solve(self,n):
        dup =(n)
        rev= 0
        while n> 0:
            last_digit=n%10
            rev = (rev*10)+last_digit
            n = n //10
        if dup == rev:
            return True
        else:
            return False




if __name__ == "__main__" :
    sol = Solution()
    inn=122211
    result=sol.solve(inn)
    print(result)
#
# Time Complexity: O(log10N + 1), as in the worst case when N is a multiple of 10 the number of digits in N is log10 N + 1. In the while loop we divide N by 10 until it becomes 0 which takes log10N iterations. In each iteration of the while loop we perform constant time operations like modulus and division and pushing elements into the vector.
#
# Space Complexity: O(1), as only a constant amount of additional memory for the reversed number regardless of size of the input number.
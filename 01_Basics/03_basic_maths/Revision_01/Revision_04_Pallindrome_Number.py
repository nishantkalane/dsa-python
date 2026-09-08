
class Solution:

    def solve(self,n):
        dup=n
        rev_no =0
        while n >0:
            last_digit= n%10
            rev_no=(rev_no*10)+last_digit
            n =n//10
        if rev_no == dup:
            return True
        else:
            return False
if __name__ == "__main__":
    solution = Solution()

    # Test your solution
    inp= 123
    result=solution.solve(inp)
    print(result)
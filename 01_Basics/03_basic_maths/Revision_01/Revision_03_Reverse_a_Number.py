
class Solution:

    def solve(self,n):
        rev_number=0
        while n > 0:
            last_digit = n %10
            # digits.append(last_digit)
            rev_number=(rev_number*10)+last_digit
            n = n//10
        return rev_number

if __name__ == "__main__":
    solution = Solution()

    # Test your solution
    inp= 32100
    result=solution.solve(inp)
    print(result)

class Solution:

    def solve(self,n):
        digits=[]
        while n > 0:
            last_digit = n % 10
            digits.append(last_digit)
            n = n //10
        return digits

if __name__ == "__main__":
    solution = Solution()

    # Test your solution
    inp=  1234
    result=solution.solve(inp)
    print(*result)


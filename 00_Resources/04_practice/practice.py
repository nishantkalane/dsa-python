class Solution:
    def solve(self,n):
        digits =[]
        while n > 0:
            last_digit = n %10

if __name__ == "__main__":
    solution = Solution()

    inp =1234
    result = Solution.solve(inp)
    print(*result)
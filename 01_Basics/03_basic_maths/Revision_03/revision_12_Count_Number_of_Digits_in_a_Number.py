class Solution:
    def solve(self, n):
        digit_count = 0
        while n > 0:
            digit_count +=1
            n //= 10
        return digit_count


if __name__ == "__main__":
    sol = Solution()

    inp = int(input("Get sum of Numbers: "))
    print(sol.solve(inp))


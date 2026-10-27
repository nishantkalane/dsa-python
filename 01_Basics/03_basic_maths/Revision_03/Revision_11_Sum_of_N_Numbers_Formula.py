class Solution:
    def solve(self, n):
        return (n*(n+1)//2)

if __name__ == "__main__":
    sol = Solution()

    inp = int(input("Get sum of Numbers: "))
    print(sol.solve(inp))

# N = O(N)
# N = O(1)
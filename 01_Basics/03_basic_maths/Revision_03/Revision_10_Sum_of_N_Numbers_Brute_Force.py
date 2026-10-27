class Solution:
    def solve(self,n):
        total = 0
        for i in range(1,n+1):
            total +=i
        return total

if __name__ == "__main__":
    sol = Solution()

    inp= int(input("Get sum of Numbers: "))
    print(sol.solve(inp))

# N = O(N)
# N = O(1)
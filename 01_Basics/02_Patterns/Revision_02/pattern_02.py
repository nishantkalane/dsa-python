class Solution:
    def pattern_02(self, n):
        for i in range(n):
            for j in range(i+1):
                print("*", end=" ")
            print()

if __name__ == "__main__":
    sol = Solution()
    n=5
    sol.pattern_02(n)


class Solution:

    def solve(self,n):
        if n<=1:
            return n
        return self.solve(n-1) + self.solve(n-2)


if __name__ == "__main__":
    solution = Solution()

    # Test your solution here
    inn=6
    print(solution.solve(inn))
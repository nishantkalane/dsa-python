class Solution:
    def solve(self, n):

        for i in range(n):
            p = ord("A")
            for j in range(i, n):
                print(chr(p), end="")
                p += 1
            print()


if __name__ == "__main__":
    sol = Solution()

    n = 5
    sol.solve(n)

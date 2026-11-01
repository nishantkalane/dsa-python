class Solution:
    def solve(self, i, n):
        if i >= n+1:
            return

        sol.solve(i + 1, n)
        print(i)

if __name__ == "__main__":
    sol = Solution()

    inp = int(input("Enter a number to print it in backwards : "))
    sol.solve(1, inp)

# TC = O(n)
# SC = O(n)
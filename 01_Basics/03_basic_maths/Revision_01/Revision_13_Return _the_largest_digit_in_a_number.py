class Solution:
    def solve(self, n):
        maxi=0
        while n > 0:
            last_digit = n %10
            if last_digit > maxi:
                maxi = last_digit
            n //=10
        return maxi



if __name__ == "__main__":
    sol = Solution()
    inp = 122098765432
    r= sol.solve(inp)
    print(r)
# TC = O(log(N))
# SC= O(1)
class Solution:
    def solve(self,s,t):
        if len(s) != len(t):
            return False
        frequency_s = {}
        for char in s:
            frequency_s[char] = frequency_s.get(char, 0) + 1
        frequency_t = {}
        for char in t:
            frequency_t[char] = frequency_t.get(char, 0) + 1
        return frequency_t == frequency_s
if __name__ == "__main__":
    sol = Solution()
    s ="paper"
    t="repan"
    print(sol.solve(s,t))
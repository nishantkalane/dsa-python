class Solution:
    def reverseString(self, s):
        l = 0
        r = len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        s = "".join(s)
        return s
if __name__ == "__main__":
    sol = Solution()

    st="Nishant"
    string_list= list(st)
    r= sol.reverseString(string_list)
    print(r)
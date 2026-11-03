class Solution:
    def reverseString(self, s):
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] !=s[r]:
                return False
            l +=1
            r -=1

        return True
if __name__ == "__main__":
    sol = Solution()

    st="adba"
    string_list= list(st)
    r= sol.reverseString(string_list)
    print(r)
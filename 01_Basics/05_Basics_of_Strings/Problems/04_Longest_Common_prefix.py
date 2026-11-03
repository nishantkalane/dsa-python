class Solution:
    def solve(self,num):
        prefix = ""
        min_len = min(len(s) for s in num)
        for j in range(min_len):
            for i in range(len(num)):
                if num[i][j] != num[0][j]:
                    return prefix
            prefix +=num[0][j]
        return prefix





if __name__ == "__main__":
    sol = Solution()

    strs = ["flower", "flow", "fly", "flight"]
    print(sol.solve(strs))
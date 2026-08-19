class Solution:
    def pattern_16(self, n):
        p=ord("A")
        for i in range(n):
            for j in range(i+1):
                print(chr(p), end="")
            p +=1
            print()



if __name__ == "__main__":
    sol = Solution()
    n=5
    sol.pattern_16(n)

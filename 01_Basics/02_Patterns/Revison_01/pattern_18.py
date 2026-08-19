class Solution:
    def pattern_18(self, n):
        p=ord("E")
        for i in range(n):
            k=p
            for j in range(i+1):
                print(chr(k),end=" ")
                k +=1
            p-=1
            print()


if __name__ == "__main__":
    sol = Solution()
    n=5
    sol.pattern_18(n)

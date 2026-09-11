class Solution:
    def pattern_22(self, inp,n):
        for i in range(n):
            for j in range(n):
                top =i
                bottom=j
                left=(n-i)-1
                right=(n-j)-1
                mini=min(top,bottom,left,right)
                print(inp-mini,end=" ")
            print()


if __name__ == "__main__":
    sol = Solution()

    n1 = 4
    n2= (n1*2)-1
    sol.pattern_22(n1,n2)


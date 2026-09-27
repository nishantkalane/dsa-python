class Solution:
    def solve(self, n1,n2):
        gcd = 1
        for i in range(1,min(n1+1,n2+1)):
            if n1 % i  == 0 and n2 % i ==0 :
                gcd = i
        return gcd


if __name__ == "__main__":
    sol = Solution()

    inp1 = 12
    inp2 = 36
    result=sol.solve(inp1, inp2)
    print(result)

#TC= O(min(n1,n2))
#SC= O(1)
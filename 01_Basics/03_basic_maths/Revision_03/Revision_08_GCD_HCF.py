class Solution:
    def solve(self,n1,n2):
        lowest = min(n1,n2)
        gcd =0
        for i in range(1,lowest):
            if n1 % i == 0 and n2 % i == 0:
                gcd = i
        return gcd


if __name__ == "__main__" :
    sol = Solution()
    inp1= int(input("Enter the first integer : "))
    inp2 = int(input("Enter the Second integer : "))
    print(sol.solve(inp1,inp2))

#TC= O(logn)
#SC= O(1)

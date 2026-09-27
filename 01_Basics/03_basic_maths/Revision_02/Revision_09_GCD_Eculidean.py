class Solution:
    def solve(self, a,b):
        while a > 0 and b > 0 :
            if a > b:
                a=a % b
            else:
                b=b % a
        if a == 0:
            return b
        else:
            return a



if __name__ == "__main__":
    sol = Solution()

    inp1 = 12
    inp2 = 36
    result=sol.solve(inp1, inp2)
    print(result)

#TC=O(log(min(a,b))
#SC: log(1)
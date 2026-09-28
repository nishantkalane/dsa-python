
class Solution:

    def solve(self,n1,n2):
        gcd=1
        for i in range(1, min(n1,n2)+1):
            if n1 % i == 0 and n2 % i==0:
                gcd=i
        return gcd
        # i = min(n1,n2)
        # while i > 1:
        #     if n1 % i == 0 and n2 % i == 0:
        #         gcd =i
        #         return gcd
        #     i -=1




if __name__ == "__main__":
    solution = Solution()

    # Test your solution
    inp1= 36
    inp2 = 18
    result=solution.solve(inp1,inp2)
    print(result)

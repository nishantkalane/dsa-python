class Solution:
    def solve(self,a,b):
        def gcd(ma,mb):
            while mb !=0:
                ma,mb = mb,ma%mb
            return ma
        total=gcd(a,b)
        lcm= a*b// total
        return lcm



if __name__ == "__main__":
    sol = Solution()

    inp_a=int(input("Give first number to calculate a LCM : "))
    inp_b=int(input("Give Second number to calculate a LCM : "))

    print(sol.solve(inp_a,inp_b))

#TC= O(logn)
#SC = O(1)


class Solution:

    def solve(self,n1,n2):
        while (n1>0 and n2>0):
            if n1>n2:
                n1 = n1 % n2
            elif n2>n1:
                n2 = n2 % n1
        if n1 ==0:
            return n2
        else:
            return n1


if __name__ == "__main__":
    solution = Solution()

    # Test your solution
    inp1= 52
    inp2 = 10
    result=solution.solve(inp1,inp2)
    print(result)

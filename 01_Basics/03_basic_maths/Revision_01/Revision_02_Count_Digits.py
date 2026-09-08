import math
class Solution:

    def solve(self,n):
        cnt= int(math.log10(n)+1)
        # while n >0:
        #     n =n//10
        #     cnt +=1
        return cnt

if __name__ == "__main__":
    solution = Solution()

    # Test your solution
    inp= 12223
    result=solution.solve(inp)
    print(result)
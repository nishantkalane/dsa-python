
class Solution:

    def solve(self,n):
        # cnt= 0
        # i =1
        # while i < n+1:
        #     if n % i ==0:
        #         cnt +=1
        #     i += 1
        # if  cnt ==2:
        #     return True
        # else:
        #     return False
        res = []
        i = 1
        while i * i < n + 1:
            if n % i == 0:
                res.append(i)
                if n // i != i:
                    res.append(n // i)
            i += 1
        if len(res) == 2:
            return True
        else:
            return False


if __name__ == "__main__":
    solution = Solution()

    # Test your solution
    inp= 3
    result=solution.solve(inp)
    print(result)

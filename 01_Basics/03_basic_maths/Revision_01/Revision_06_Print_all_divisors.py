
class Solution:

    def solve(self,n):
        # i=1
        # res=[]
        # while i < n+1:
        #     if n % i==0:
        #         res.append(i)
        #     i +=1
        # return res
        i =1
        res=[]
        while i*i<n+1:
            if n % i == 0:
                res.append(i)
                if n//i !=i:
                    res.append(n//i)
            i +=1
        return res

if __name__ == "__main__":
    solution = Solution()

    # Test your solution
    inp= 36
    result=solution.solve(inp)
    result1=sorted(result)
    print(*result1)
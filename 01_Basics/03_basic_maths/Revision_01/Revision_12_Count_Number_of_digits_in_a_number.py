class Solution:
    def solve(self, n):
        cnt=0
        while n > 0:
            cnt +=1
            n //=10
        return cnt



if __name__ == "__main__":
    sol = Solution()
    inp = 122
    r= sol.solve(inp)
    print(r)
# TC = O(log(N))
# SC= O(1)
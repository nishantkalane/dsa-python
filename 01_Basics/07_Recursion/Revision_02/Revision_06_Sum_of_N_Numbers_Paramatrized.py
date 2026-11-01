class Solution:
    def solve(self,n,sum):

        if n==0:
            return sum
        return self.solve(n-1,sum +n)


if __name__ == "__main__" :
    sol= Solution()

    inp= int(input("Enter n: "))

    print(sol.solve(inp,0))
# TC= O(log(n))
# SC= O(1)
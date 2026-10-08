class Solution:
    def solve(self,n):
        cnt = 0
        while n > 0:
            cnt +=1
            n //=10
        print(cnt)

if __name__ == "__main__" :
    sol= Solution()

    inp= int(input("Enter a number to separate it's digit: "))

    sol.solve(inp)

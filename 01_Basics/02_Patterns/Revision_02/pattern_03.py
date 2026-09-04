class Solution:
    def pattern_03(self,n):
        for i in range(n):
            p=1
            for j in range(i+1):
                print(p, end=" ")
                p +=1
            print()


if __name__ == "__main__" :
    sol=Solution()

    n=4
    sol.pattern_03(n)

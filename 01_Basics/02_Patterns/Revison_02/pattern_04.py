class Solution:
    def pattern_04(self,n):
        p=1
        for i in range(n):
            for j in range(i+1):
                print(p,end="")
            print()
            p +=1




if __name__ == "__main__" :
    sol=Solution()

    n=5
    sol.pattern_04(n)
class Solution:
    def pattern_22(self,n,k):
       for i in range(k):
           for j in range(k):
               print(n-min(i,k-j-1,j,k-i-1),end="")
           print()



if __name__ == "__main__" :
    sol=Solution()

    n=4
    k=(2*n)-1
    sol.pattern_22(n,k)
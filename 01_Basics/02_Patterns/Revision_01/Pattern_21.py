class Solution:
    def pattern_21(self,n):
       for i in range(n):
           for j in range(i):
               if i == 0 or j ==0 or i==n-1 or j == n-1:
                   print("*", end=" ")
               else:
                    print(" ",end=" ")
           for j in range(i,n):
               if i == 0 or j == 0 or j == n-1:
                   print("*", end=" ")
               else:
                   print(" ", end=" ")
           print()





if __name__ == "__main__" :
    sol=Solution()

    n=4
    sol.pattern_21(n)
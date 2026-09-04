class Solution:
    def pattern_12(self,n):

        for i in range(n):
            p=1
            for j in range(i+1):
                print(p,end=" ")
                p+=1
            for j in range(i,n-1):
                print(" ",end=" ")
            for j in range(i,n-1):
                print(" ",end=" ")
            for j in range(i+1):
                p -= 1
                print(p,end=" ")

            print()

if __name__ == "__main__":
    sol =Solution()
    n=4
    sol.pattern_12(n)
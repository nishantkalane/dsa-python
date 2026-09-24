class Solution:
    def solve(self, n,s):
        p=s
        for i in range(n):
            k=p
            for j in range(i+1):
                print(chr(k),end=" ")
                k +=1
            p -=1
            print()

if __name__ == "__main__":
    sol = Solution()

    n =  6
    start= (65 + n)-1
    sol.solve(n,start)

#TC=O(N^2) as we print it for n times for each character and two loops inside each other
#SC = O(1)
class Solution:
    def solve(self,i ,n):
        if i >=n+1:
            return
        self.solve(i+1,n)
        print(i)

if __name__ == "__main__" :
    sol= Solution()

    inp= int(input("Enter a number to separate it's digit: "))

    sol.solve(1,inp)
# TC= O(n)
# SC= O(n)
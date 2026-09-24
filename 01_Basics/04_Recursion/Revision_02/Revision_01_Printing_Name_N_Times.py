class Solution:
    def solve(self,i, n,nam):
        if i >n:
            return
        print(nam)
        self.solve(i+1,n,nam)


if __name__ == "__main__":
    sol = Solution()

    n = int(input("Enter number of times you want to print your name : "))
    name=input("Enter Name: ")
    sol.solve(1,n,name)

#TC = O(n)
#SC = O(n)
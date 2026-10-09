class Solution:
    def solve(self, na,n):
        if n ==0:
            return
        print(na)
        self.solve(na,n-1)


if __name__ == "__main__":
    sol = Solution()
    name=input("Enter your name: ")
    n=int(input("Enter a number to print your name N time: "))
    sol.solve(name,n)

# TC = O(N)
# SC = O(N)
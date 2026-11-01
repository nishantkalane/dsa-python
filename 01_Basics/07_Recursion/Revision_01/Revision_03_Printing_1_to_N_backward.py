class Solution:
    def solve(self,i,n):
        if i ==0:
            return()
        self.solve(i-1,n)
        print(i , end =" ")


if __name__ == "__main__":
    solution = Solution()

    # Test your solution here
    inp =int(input("Till what number you want to print from 1? "))
    solution.solve(inp,inp)

# TC= O(N), we print every number from 1 to N using recursion
# SC = O(N) Stack space used for recursive call

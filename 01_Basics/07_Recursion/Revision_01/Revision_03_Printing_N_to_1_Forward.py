class Solution:
    def solve(self,i,n):
       if i <= 0:
           return
       print(i)
       self.solve(i-1,n)


if __name__ == "__main__":
    solution = Solution()

    # Test your solution here
    inp =int(input("From what number you want to print down to 1 ? "))
    solution.solve(inp,inp)

#TC : O(N) as recursion happens n times
#SC : O(N) as stack is used

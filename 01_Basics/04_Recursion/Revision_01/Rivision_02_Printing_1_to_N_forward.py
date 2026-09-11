class Solution:
    def solve(self,i,n):

        if i ==n+1:
            return()
        print(i)
        self.solve(i+1,n)



if __name__ == "__main__":
    solution = Solution()

    # Test your solution here
    inp =int(input("From to what number you want to print "))
    solution.solve(1,inp)

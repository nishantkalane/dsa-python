

class Solution:
    def solve(self,i,n):
        if i ==n:
            return
        print("nish")
        self.solve(i+1,n)


if __name__ == "__main__":
    solution = Solution()

    # Test your solution here
    inp =int(input("How many times you want to print your name? "))
    solution.solve(0,inp)





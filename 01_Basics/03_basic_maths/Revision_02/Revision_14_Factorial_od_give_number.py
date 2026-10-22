class Solution:
    def solve(self,n):
        factorial=1
        for i in range(1,n+1):
            factorial *=i
        return factorial




if __name__ == "__main__":
    sol = Solution()

    inp=int(input("Which number's factor you want: "))
    print(sol.solve(inp))

#TC =O(n)
#SC =O(1)
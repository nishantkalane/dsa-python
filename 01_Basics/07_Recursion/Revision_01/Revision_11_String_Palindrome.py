class Solution:
    def solve(self,i, st, n):
        if i > n//2:
            return True
        if st[i] != st[n-i-1]:
            return False
        return self.solve(i+1,st,n)
if __name__ == "__main__":
    sol = Solution()
    inp = input("Enter string to check if it is a palindrome or not: ")
    lenn= len(inp)
    r= sol.solve(0,inp,lenn)
    print(r)

# TC = O(N)
# SC= O(1)

class Solution:
    def solve(self, l,r, arr):
        if l >=r:
            return arr
        arr[l],arr[r] = arr[r],arr[l]
        return self.solve(l+1,r-1,arr)


if __name__ == "__main__":
    sol = Solution()
    inp = list(map(int,input("Enter array, with number's separated by ',' : ").split(',')))
    left=0
    right=len(inp)-1
    r = sol.solve(left,right,inp)
    print(r)

# TC = O(n)
# SC= O(n)

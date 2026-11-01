class Solution:
    def solve(self,i, arr,n):
        if i > n//2:
            return arr
        arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
        return self.solve(i+1,arr,n)


if __name__ == "__main__":
    sol = Solution()
    arry = list(map(int,input("Enter numbers separated by ',': ").split(",")))
    inp = len(arry)
    r= sol.solve(0,arry,inp)
    print(r)

# TC = O(N)
# SC= O(N)

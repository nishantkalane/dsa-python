class Solution:
    def solve(self, arr,l,r):
        if l>r:
            return arr
        arr[l],arr[r]=arr[r],arr[l]
        return self.solve(arr,l+1,r-1)



if __name__ == "__main__":
    sol = Solution()

    array = list(map(int, input("Enter numbers in array separated by ',' : ").split(',')))
    lenn=len(array)
    left=0
    right=lenn-1
    result=(sol.solve(array,left,right))
    print(*result)

#TC=O(n)
#SC=O(n)

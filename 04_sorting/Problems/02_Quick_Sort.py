class Solution:

    def partition(arr,low,high):
        pivot = arr[low]
        i= low
        j = high
        while i < j:
            #find an element smaller than or equal to pivot
            while i <= high and arr[i] <= pivot:
                i +=1

            #find an element greater than or pivot
            while j > low and arr[j] > pivot:
                j -= 1

           # swap misplaced elements
            if i < j:
                arr[i], arr[j] = arr[j],arr[i]
        # place pivot in its correct position
        arr[low], arr[j] = arr[j], arr[low]
        return j



    def sort(self,arr,low,high):
        if low<high:

            part = Solution.partition(arr,low,high)
            self.sort(arr,low,part-1)
            self.sort(arr,part+1,high)

if __name__ ==  "__main__":
    sol = Solution()
    array = [1,4,5,2,9,2,1,9]
    left = 0
    high = len(array)-1
    sol.sort(array,left,high)
    print(array)

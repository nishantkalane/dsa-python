

#mistake: the base condition shall use // not / while dividing by 2 so to get int, and have brackets around high and low because otherwise division will get higher precedence.


class Solution:

    def merge(self,arr,low,mid,high):
        temp = []
        left = low
        right = mid+1
        while left <= mid and right <=high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left +=1
            else:
                temp.append(arr[right])
                right +=1
        while left <= mid:
            temp.append(arr[left])
            left += 1
        while right <= high:
            temp.append(arr[right])
            right += 1
        for i in range(low,high+1):
            arr[i] = temp[i-low]


    def merge_sort(self, arr, low, high):
        if low >= high:
            return
        mid = (low + high) // 2
        self.merge_sort(arr, low, mid)
        self.merge_sort(arr, mid + 1, high)
        self.merge(arr,low,mid,high)



if __name__ == "__main__":
    sol = Solution()
    array = [5,2,1,3,1,2,7,8,9,10]
    lowest = 0
    highest = len(array)-1
    sol.merge_sort(array,lowest,highest)
    print(array)


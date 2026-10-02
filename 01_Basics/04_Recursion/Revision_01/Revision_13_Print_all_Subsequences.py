
class Solution:

    def solve(self,i,arr,ls):
        n =len(arr)
        if i >=n:
            print(ls)
            return
        #take
        ls.append(arr[i])
        self.solve(i+1,arr,ls)
        #return
        ls.pop()
        self.solve(i+1,arr,ls)





if __name__ == "__main__":
    solution = Solution()

    # Test your solution here
    array =list(map(int,input("Enter numbers seprated by ',' : ").split(',')))
    solution.solve(0,array,[])
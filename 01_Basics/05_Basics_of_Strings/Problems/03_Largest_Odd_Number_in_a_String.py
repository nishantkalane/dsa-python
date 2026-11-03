class Solution:
    def solve(self,num):
        for i in range(len(num)-1,-1,-1):
            if int(num[i]) % 2 !=0:
                result = num[:i+1]
                return result.lstrip("0")
        #case in situations of no odd digit
        return ""



if __name__ == "__main__":
    sol = Solution()

    num= "054212543"
    print(sol.solve(num))

class Solution:
    def solve(self,i, n1):
        div =[]
        square_root =n1**0.5
        while i < square_root:  #or i*i < n+1
            if n1 % i ==0:
                div.append(i)
                if n1//i !=i:
                    div.append(n1//i)
            i+=1
        return div



if __name__ == "__main__":
    sol = Solution()

    inp1=36
    result=sol.solve(1,inp1)
    result2=sorted(result)
    print(*result2)
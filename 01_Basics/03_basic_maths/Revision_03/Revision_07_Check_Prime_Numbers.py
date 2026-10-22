class Solution():
    def solve(self,n):
        cnt=0
        i=1
        while i*i <=n:
            if n % i == 0:
                cnt +=1
                if n//i and i*i !=n:
                    cnt +=1
            i+=1
        if cnt == 2:
            return True
        else:
            return False


if __name__ == "__main__":
    sol = Solution()

    inp = int(input("Enter a number to check if it's prime: "))
    print(sol.solve(inp))

#tc =O(squrt n)
#sc =O(1)
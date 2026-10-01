class Solution:
    def solve(self,i, n,summ):
        while i*i <=n:
            if n % i ==0:
                summ +=i
                if n//i !=i and n//i !=n:
                    summ +=n//i
            i +=1
        if summ==n:
            return True
        else:
            return False


if __name__ == "__main__":
    sol = Solution()
    inp = int(input("Enter number: "))
    r= sol.solve(1,inp,0)
    print(r)

# TC =o(underoot of N)
# SC= O(N)
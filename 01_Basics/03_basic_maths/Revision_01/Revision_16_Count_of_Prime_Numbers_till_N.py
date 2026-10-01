class Solution:
    def solve(self, n):
        prime_count=0
        for j in range(1,n):
            cnt =0
            i=1
            while i*i <=j:
                if j%i==0:
                    cnt+=1
                    if j//i !=i:
                        cnt+=1
                i +=1
            if cnt == 2:
                prime_count +=1
        return prime_count



if __name__ == "__main__":
    sol = Solution()
    inp = int(input("Enter number: "))
    r= sol.solve(inp)
    print(r)

# TC =o(n * under-root of n)
# SC= O(N)


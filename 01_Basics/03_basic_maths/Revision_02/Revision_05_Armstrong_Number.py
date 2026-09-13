class Solution():
    def solve(self, n):
        dup=n
        arm_no =0
        power =len(str(n))
        while n >0 :
            last_digit = n %10
            arm_no +=(last_digit**power)
            n = n//10

        if arm_no==dup:
            return True
        else:
            return False

if __name__ == "__main__":
    sol = Solution()
    n = 1634
    result = sol.solve(n)
    print(result)

# TC : O(log10(N)+1) where N is the input number. The time complexity is determined by the number of digits in the input integer N
       # In the worst case when Nis multiple of 10 the of digits in N is log10 N+1
# SC : O(1) as only a constant amount of additional memory for the reversed number regardless of size of input number

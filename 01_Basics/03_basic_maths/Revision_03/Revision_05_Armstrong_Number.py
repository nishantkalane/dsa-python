class Solution:
    def solve(self,n):
        duplicate = n
        length_of_input=len(str(n))
        middle_checker = 0
        while n >0:
            last_digit = n % 10
            middle_checker += last_digit**length_of_input
            n //= 10
        if duplicate==middle_checker:
            return True
        return False



if __name__ == "__main__":
    sol = Solution()

    inp=int(input("Check Armstrong Number: "))
    result=sol.solve(inp)
    print(result)
#TC = O(log(n)+1)
#SC = O(1)
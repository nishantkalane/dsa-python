class Solution:
    def solve(self,n):
        divisors = []
        i=1
        while i*i <= n:
            if n % i == 0:
                divisors.append(i)
                if n//i and i*i != n:
                    divisors.append(n//i)
            i +=1
        sorted1 = sorted(divisors)
        return sorted1


if __name__ == "__main__":
    sol = Solution()

    get_div = int(input("Get input for the factors :  "))
    res = sol.solve(get_div)
    print(res)

# TC = O(sqrt n)
#SC= O(1)

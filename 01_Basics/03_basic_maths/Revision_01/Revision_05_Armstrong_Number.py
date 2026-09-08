
class Solution:

    def solve(self,n):
        dup=n
        length=len(str(n))
        armstrong_number=0
        while n > 0:
            last_digit=n%10
            armstrong_number += last_digit**length
            n //=10
        if armstrong_number ==dup:
            return True
        else:
            return False

if __name__ == "__main__":
    solution = Solution()

    # Test your solution
    inp= 32
    result=solution.solve(inp)
    print(result)
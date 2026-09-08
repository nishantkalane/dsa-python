"""
Problem:
Get the GCD or HCF of two numbers
input: n1=9 and n2=12
output: 3

Platform:
Strivers sheet

Topic:
GCD, HCF

Difficulty:
medium

Approach:

Euclidean Algorithm:
The Euclidean Algorithm is a method for finding the greatest common divisor (GCD) of two numbers. It operates on the principle that the GCD of two numbers remains the same even if the smaller number is subtracted from the larger number.

To find the GCD of n1 and n2 where n1 > n2:

Repeatedly subtract the smaller number from the larger number until one of them becomes 0.
Once one becomes 0, the other is the GCD of the original numbers.
Example: n1 = 20, n2 = 15

gcd(20, 15) = gcd(20 - 15, 15) = gcd(5, 15)
gcd(5, 15) = gcd(15 - 5, 5) = gcd(10, 5)
gcd(10, 5) = gcd(10 - 5, 5) = gcd(5, 5)
gcd(5, 5) = gcd(5 - 5, 5) = gcd(0, 5)
Hence, return 5 as the GCD


Time Complexity: O(log(min(N1, N2))) as the Euclidean algorithm repeatedly replaces the larger number with the remainder of dividing it by the smaller number. This rapidly reduces the problem size, requiring at most a logarithmic number of iterations.

Space Complexity: O(1) as the space complexity remains constant and independent of the input size. Only a fixed amount of memory is required to store the integer variable
Date Solved:
-07-SEP-2026

Key Takeaway:
Repeatedly replace the larger number with its remainder until one becomes 0; the remaining non-zero number is the GCD, in O(log(min(n1,n2))) time.


"""


class Solution:

    def solve(self, n1,n2):
        while(n1 >0 and n2 >0):
            if (n1>n2):
                n1=n1%n2
            else:
                n2 = n2 % n1
        if n1 == 0:
            return n2
        return n1





if __name__ == "__main__":
    solution = Solution()

    # Test your solution
    inp1 = 12
    inp2 = 16
    result = solution.solve(inp1,inp2)
    print(result)

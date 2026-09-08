"""
Problem:
Print the divisors of a number
N= 36
output: 1, 2, 3, 4, 6, 9, 12, 18, 36

Platform:
Strivers sheet

Topic:
Divisors printing

Difficulty:
medium

Approach:
Linear method:
    loop in range form 1 to n
    check if diving n by i results in 0
    if yes append it to list
    print the list

optimal square root method:
    use while loop to check the square root is less than n  that is loop till eg 6*6 is less than 36
    then check if n is divisible by i if yes append it to a empty list
    in the indented if condition check now if n/i is not equal to i so that i doesn't come twice thus we get the another side of the mutiples
    increment i
    sort the list and assign it to a  variable
    return that variable and print it


Linear Method:
Time Complexity: O(N), we check for every number from 1 to N.
Space Complexity: O(N), extra space used for storing divisors.

Optimal Method:
Time Complexity: O(sqrt(N)+ log sqrt(N)), we check for every number between 1 and sqaure root of N.
Space Complexity: O(2*sqrt(N)), extra space used for storing divisors.

Date Solved:
-07-SEP-2026

Mistake:
-using // two times give int divisor
- not keeping the second if indented under first if in that condition that calculation happens only when the divisor is there
- printing of  n //i and not i in second loop
- to sort assign the sorted() function to a variable
Key Takeaway:
-using // two times give int divisor
- not keeping the second if indented under first if in that condition that calculation happens only when the divisor is there
- printing of  n //i and not i in second loop
- to sort assign the sorted() function to a variable

"""

class Solution:

    def solve(self,n):
        """Getting Divisors of a  Number"""
        # TC = O(n) as it goes linearly
        res =[]
        # for i in range(1,n+1):
        #     if n % i == 0:
        #         res.append(i)

        # till square root method :
        i=1
        while i*i <=n:
            if n % i ==0:
                res.append(i)
                if i !=n // i:
                    res.append(n//i)
            i +=1
        res= sorted(res)
        return res

if __name__ == "__main__":
    solution = Solution()

    # Test your solution
    inp= 36
    result=solution.solve(inp)

    print(f"Divisors for {inp} are", *result )
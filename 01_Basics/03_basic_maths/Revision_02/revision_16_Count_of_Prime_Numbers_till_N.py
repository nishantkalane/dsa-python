class Solution:
    def solve(self,n):
        main_counter =0

        for m in range(1,n+1):
            i=1
            counter_checker = 0
            while i*i <=m:
                if m % i ==0 :
                    counter_checker +=1
                    if m//i and i*i !=m:
                        counter_checker +=1
                i +=1
            if counter_checker == 2:
                main_counter += 1
        return main_counter




if __name__ == "__main__":
    sol = Solution()

    inp=int(input("Enter a Prime Number counts till N: "))
    print(sol.solve(inp))

# TC = O(nrootn)
# SC = O(1)
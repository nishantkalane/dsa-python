from functools import reduce

#reduce() repeatedly combines values into one final value

product_of_all = reduce(
    lambda a,b: a*b,
    [1,2,3,4]
)

print(product_of_all)

sum_of_all =reduce(
    lambda a,b: a+b,
    [1,2,3,4,5,6,7,8,9]

)

print(sum_of_all)
#groupby() groups consecutive equal elements

from itertools import groupby


for key, group in groupby("aabbbaaaa,ccccc"):
    print(key,list(group))
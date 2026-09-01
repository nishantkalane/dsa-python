groups={
    "s":1,
}

# groups["a"].append(2) gives a error because a doesn't exist.

#A defaultdict is basically a dictionary that automatically creates a default value when a key doesn't exist.

from collections import defaultdict
groups=defaultdict(list)

groups["a"].append(2)
groups["a"].append(3)
print(groups)

#It is extremly useful when I will be learning graphs

 # a namedtuple gives names to the fields of a tuple

from collections import namedtuple
Point=namedtuple("Point","x y")

p= Point((3,4),(4,3))

print(p.x)
print(p.y)

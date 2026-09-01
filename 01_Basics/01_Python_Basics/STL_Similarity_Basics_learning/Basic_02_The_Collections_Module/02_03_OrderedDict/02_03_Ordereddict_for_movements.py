from collections import OrderedDict

od= OrderedDict(
    [
        ("a",1),
        ("b",2),
        ("c",3)

    ]
)

od.move_to_end("a")
print(od)
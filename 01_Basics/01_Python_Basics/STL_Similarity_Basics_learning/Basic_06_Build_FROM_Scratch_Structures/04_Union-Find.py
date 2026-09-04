class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            self.parent[root_b] = root_a

uf = UnionFind(5)

uf.union(0, 1)
uf.union(1, 2)

print(uf.find(0) == uf.find(2))
print(uf.find(0) == uf.find(3))
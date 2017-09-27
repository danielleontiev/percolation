class UnionFind:

    def __init__(self, size):
        self.size = size
        self.id = list(range(size))
        self.depth = [1] * size


    def root(self, i):
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i


    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if self.depth[i] < self.depth[j]:
            self.id[i] = j
            self.depth[j] += self.depth[i]
        else:
            self.id[j] = i
            self.depth[i] += self.depth[j]


    def find(self, p, q):
        return self.root(p) == self.root(q)


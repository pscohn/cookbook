#!/usr/bin/env python3

class QuickFind:
    def __init__(self, n):
        self.ids = [i for i in range(0,n)]

    def connected(p, q):
        return self.ids[p] == self.ids[q]

    def union(p, q):
        pid = self.ids[p]
        for i in self.ids:
            if self.ids[i] == pid:
                self.ids[i] = self.ids[q]

class QuickUnion:
    ''' Lazy approach.'''
    def __init__(self, n):
        self.ids = [i for i in range(0,n)]

    def get_root(self, i):
        while self.ids[i] != i:
            i = self.ids[i]
        return i

    def connected(self, p, k):
        return self.get_root(p) == self.get_root(k)

    def union(self, p, k):
        self.ids[self.get_root(p)] = self.get_root(k)

class WeightedQuickUnion:
    def __init__(self, n):
        self.ids = [i for i in range(0,n)]
        self.sizes = [1 for _ in self.ids]

    def get_root(self, i):
        while self.ids[i] != i:
            self.ids[i] = self.ids[self.ids[i]] # path compression
            i = self.ids[1]
        return i

    def connected(self, p, q):
        return self.get_root(p) == self.get_root(q)

    def union(self, p, q):
        i = self.get_root(p)
        j = self.get_root(q)
        if i == j: return
        if self.sizes[i] <= self.sizes[j]:
            self.ids[i] = j
            self.sizes[j] += self.sizes[i]
        else:
            self.ids[j] = i
            self.sizes[i] += self.sizes[j]

if __name__ == '__main__':
    main()


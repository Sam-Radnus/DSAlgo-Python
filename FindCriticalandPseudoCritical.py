import os
import math
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv: return False
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = self.parent[pv]
        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = self.parent[pu]
        else:
            self.rank[pu] += 1
            self.parent[pv] = pu
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = [[u, v, w, i] for i, [u, v, w] in enumerate(edges)]  # Add original indices of edge to edges array
        edges.sort(key=lambda x: x[2])  # Sort in increasing order of weight

        # O(E)
        def kruskal(n, edges, bannedIdx, includeIdx):
            uf = UnionFind(n)
            totalWeight = 0
            if includeIdx != -1:#include index
                u, v, w, _ = edges[includeIdx]
                uf.union(u, v)
                totalWeight += w
                n -= 1

            for i, (u, v, weight, _) in enumerate(edges):
                if i == bannedIdx: continue
                if uf.union(u, v):
                    totalWeight += weight
                    n -= 1
                if n == 1: break  # A bit optimize since we found enough n-1 edges
            return math.inf if n > 1 else totalWeight

        criticalEdges = []
        mstWeight = kruskal(n, edges, -1, -1)
        for i in range(len(edges)):  # O(E * E)
            totalWeight = kruskal(n, edges, i, -1)
            if totalWeight > mstWeight:  # the mst increasing -> ith edge is critical
                criticalEdges.append(edges[i][3])  # add original index

        pseudoCriticalEdges = []
        for i in range(len(edges)):  # O(E * E)
            if edges[i][3] in criticalEdges: continue  # We only care non-critical edges
            totalWeight = kruskal(n, edges, -1, i)
            if totalWeight == mstWeight:  # the mst the same -> ith edge is pseudo-critical i.e it may appear or may not appear
                pseudoCriticalEdges.append(edges[i][3])  # add original index

        return [criticalEdges, pseudoCriticalEdges]
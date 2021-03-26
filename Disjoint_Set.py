class Node:
    def __init__(self, x):
        self.parent = x
        self.rank = 1


class Disjoint_Set:
    def __init__(self):
        self.set = {}
        self.max = 0

    def make_set(self, numList):
        for x in numList:
            node = Node(x)
            self.set[x] = node

    def find(self, x):
        if self.set[x].parent != x:
            self.set[x].parent = self.find(self.set[x].parent)
        return self.set[x].parent

    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent == y_parent:
            return
        if self.set[x_parent].rank <= self.set[y_parent].rank:
            self.set[x_parent].parent = y_parent
            self.set[y_parent].rank += self.set[x_parent].rank
            if self.max < self.set[y_parent].rank:
                self.max = self.set[y_parent].rank
        else:
            self.set[y_parent].parent = x_parent
            self.set[x_parent].rank += self.set[y_parent].rank
            if self.max < self.set[x_parent].rank:
                self.max = self.set[x_parent].rank

    def __str__(self):
        for x in self.set:
            self.find(x)
        s = {}
        for x in self.set:
            if self.set[x].parent not in s:
                s[self.set[x].parent] = {x}
            else:
                s[self.set[x].parent].add(x)
        return s.__str__()


# Friend Circle  Queries on HackerRank
# Use the idea of Disjoint set
def maxCircle(queries):
    djSet = Disjoint_Set()
    for query in queries:
        djSet.make_set(query)

    ans = []
    for query in queries:
        djSet.union(query[0], query[1])
        ans.append(djSet.max)
    return ans


def main():
    queries = [[1, 2], [3, 4], [1, 3], [5, 7], [5, 6], [7, 4]]
    print(maxCircle(queries))


main()

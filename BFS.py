class Graph:
    def __init__(self, n):
        self.vertices = []
        for _ in range(n):
            vertex = Vertex()
            self.vertices.append(vertex)

    def connect(self, x, y):
        vertexX, vertexY = self.vertices[x], self.vertices[y]
        vertexX.add(y)
        vertexY.add(x)

    def find_all_distances(self, s):
        queue = [s]
        self.vertices[s].dist = 0
        visited = [False] * len(self.vertices)
        visited[s] = True
        while queue:
            idx = queue.pop(0)
            parent = self.vertices[idx]
            for idx in parent.adjList:
                if not visited[idx]:
                    if parent.dist == -1:
                        self.vertices[idx].dist = 1
                    else:
                        self.vertices[idx].dist = parent.dist + 1
                    queue.append(idx)
                    visited[idx] = True
        ans = [vertex.dist * 6 if vertex.dist > 0 else vertex.dist * 1 for vertex in self.vertices]
        ans.remove(0)
        return ans


class Vertex:
    def __init__(self):
        self.adjList = list()
        self.dist = -1

    def add(self, toEdge):
        self.adjList.append(toEdge)


# HackerRank Shortest Reach in a Graph
# @para t: # of test cases
# @para n, m: # of vertices and edges of the undirected graph
# @ in the next m lines, [x, y] is the edge between x and y
# @para s: the source
# TODO: find the distances from the source to each other vertex of graph
#        6: default length of each edge
#       -1: no path from source
def main():
    t = int(input())
    for _ in range(t):
        n, m = [int(value) for value in input().split()]
        graph = Graph(n)
        for _ in range(m):
            x, y = [int(x) for x in input().split()]
            graph.connect(x-1, y-1)
        s = int(input())
        print(graph.find_all_distances(s-1))


main()
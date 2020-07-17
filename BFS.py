from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)
    
    def bfs(self, vertex):
        q = deque()
        seen = set()

        q.append(vertex)
        seen.add(vertex)

        while q:
            node = q.popleft()
            print(node, end=' ')

            for edge in self.graph[node]:
                if edge not in seen:
                    q.append(edge)
                    seen.add(edge)

if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(0,1)
    graph.add_edge(0,2)
    graph.add_edge(1,2)
    graph.add_edge(2,0)
    graph.add_edge(2,3)
    graph.add_edge(2,3)

    print("BFS: ", end=' ')
    graph.bfs(2)
    print()

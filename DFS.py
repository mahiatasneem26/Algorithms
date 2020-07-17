from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)
    
    def dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')

        for edge in self.graph[vertex]:
            if edge not in visited:
                self.dfs_recursive(edge, visited)
    
    def dfs_iterative(self, vertex,visited):
        stack = [vertex]

        while stack:
            node = stack.pop()

            if node not in visited:
                print(node, end=' ')
                visited.add(node)

            for edge in self.graph[vertex]:
                if edge not in visited:
                    stack.append(edge)
    
    def dfs(self):
        V = len(self.graph)
        visited1 = set()
        visited2 = set()

            
        print('Recursive: ', end=' ')
        for i in range(V):
            if i not in visited1:
                self.dfs_recursive(i, visited1)
        print()

        print('Iterative: ', end=' ')
        for i in range(V):
            if i not in visited2:
                self.dfs_iterative(i, visited2)
        print()


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(1,0)
    graph.add_edge(2,1)
    # graph.add_edge(1,2)
    # graph.add_edge(2,0)
    graph.add_edge(3,4)
    graph.add_edge(4,0)

    print("DFS: ")
    graph.dfs()
    print()

"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        # make a queue
        q = Queue()
        # enqueue our starting node
        q.enqueue(starting_vertex)

        # make a set to track if we've been here before
        visted = set()

        # while our queue is not empty
        while q.size() > 0:
            # dequeue whatever is at the front of our line, this is our current_node
            current_node = q.dequeue()
            # if we havent visted this node yet,
            if current_node not in visted:
                # mark as visited
                visted.add(current_node)
                print(current_node)
                # get its neighbors
                neighbors = self.get_neighbors(current_node)
                # for each of the neighbors add to the queue
                for neighbor in neighbors:
                    # add to queue
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        # make a stack
        s = Stack()
        # push on our starting node
        s.push(starting_vertex)
        # make a set to track if we've been here before
        visited = set()
        # while our stack is not empty
        while s.size() > 0:
            # pop off whatever's on top, this is current_node
            current_node = s.pop()
            # if we haven't visited this vertex before
            if current_node not in visited:
                # mark as visited
                visited.add(current_node)
                print(current_node)
                # get its neighbors
                neighbors = self.get_neighbors(current_node)
                # for each of the neighbors
                for neighbor in neighbors:
                    # add to our stack
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if starting_vertex in self.vertices:
            print(starting_vertex)
            visited.add(starting_vertex)
            for vertex in self.get_neighbors(starting_vertex):
                if vertex not in visited:
                    self.dft_recursive(vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        visited = set()

        q.enqueue([starting_vertex])

        if starting_vertex == destination_vertex:
            return [starting_vertex]

        while q.size() > 0:
            direction = q.dequeue()
            node = direction[-1]

            if node not in visited:
                visited.add(node)

                for vertex in self.get_neighbors(node):
                    new_direct = list(direction)
                    new_direct.append(vertex)

                    q.enqueue(new_direct)

                    if vertex == destination_vertex:
                        return new_direct

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = set()
        direction = [starting_vertex]
        if starting_vertex not in self.vertices or destination_vertex not in self.vertices:
            return None
        if starting_vertex == destination_vertex:
            return direction
        s = Stack()
        s.push(direction)

        while s.size() > 0:
            direction = s.pop()
            node = direction[-1]
            if node not in visited:
                visited.add(node)
                for vertex in self.get_neighbors(node):
                    new_direct = list(direction)
                    new_direct.append(vertex)
                    s.push(new_direct)
                    if vertex == destination_vertex:
                        return new_direct

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, direction=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited == None:
            visited = set()

        if direction == None:
            direction = []

        if starting_vertex not in visited:
            visited.add(starting_vertex)
            direct_copy = direction.copy()
            direct_copy.append(starting_vertex)

            if starting_vertex == destination_vertex:
                return direct_copy

            for edge in self.get_neighbors(starting_vertex):
                new_direct = self.dfs_recursive(
                    edge, destination_vertex, visited=visited, direction=direct_copy)
                if new_direct is not None:
                    return new_direct


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))

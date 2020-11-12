"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
from collections import deque


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
        if v1 not in self.vertices or v2 not in self.vertices:
            print('one or more vertecies does not exist')
            return
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
        queue = deque()
        visited = set()
        # edge case check if node given is a vertex in the graph
        if starting_vertex not in self.vertices:
            print('vertex not in graph')
            return
        # add the starting vertex to the queue to start the traversal
        queue.append(starting_vertex)

        # loop to run while there is still a vertex that has not been traversed
        while len(queue) > 0:
            # sets the current node to the node on the left side of the queue, and removes it from the queue
            currNode = queue.popleft()
            # checks if the current node has been visited before
            if currNode not in visited:
                # add the current node to the visited set so that it does not get added again
                visited.add(currNode)
                print(currNode)
                # checks the node's set neighbors, and adds them to the end of the queue to be checked and prited
                for neighbor in self.vertices[currNode]:
                    queue.append(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = deque()
        visited = set()
        # edge case check if node given is a vertex in the graph
        if starting_vertex not in self.vertices:
            print('vertex not in graph')
            return
        # add the starting vertex to the stack to start the traversal
        stack.append(starting_vertex)

        # loop to run while there is still a vertex that has not been traversed
        while len(stack) > 0:
            # sets the current node to the node on the right side of the stack, and removes it from the queue
            currNode = stack.pop()
            # checks if the current node has been visited before
            if currNode not in visited:
                # add the current node to the visited set so that it does not get added again
                visited.add(currNode)
                print(currNode)
                # checks the node's set neighbors, and adds them to the end of the stack to be checked and prited
                for neighbor in self.vertices[currNode]:
                    stack.append(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # edge case that the given vertex is not in the graph
        if starting_vertex not in self.vertices:
            print('vertex not in graph')
            return
        # set used in helper function to keep track of visited vertecies to avoid stack overflow
        visited_verts = set()

        # helper function that handles the recursive call for the DFT, it takes a vertex and the set of visited verticies
        def dft_helper(starting_vertex, visited):
            # check the visited set for vertex
            if starting_vertex not in visited:
                print(starting_vertex)
                # add vertex to visited set
                visited_verts.add(starting_vertex)
                # check for connected vertecies
                if self.vertices[starting_vertex]:
                    # call the helper function on each vertex connected to the vertex passed into the helper
                    for vertex in self.vertices[starting_vertex]:
                        dft_helper(vertex, visited_verts)
            else:
                pass
        # call the helper function with the starting vertex and the set of visited vertecies
        dft_helper(starting_vertex, visited_verts)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = deque()
        visited = set()

        queue.append([starting_vertex])

        while len(queue) > 0:
            currPath = queue.popleft()
            # sets the current node to the end of the starting vertex list
            currNode = currPath[-1]

            if currNode == destination_vertex:
                return currPath
            if currNode not in visited:
                visited.add(currNode)
                for neighbor in self.vertices[currNode]:
                    newPath = list(currPath)
                    newPath.append(neighbor)
                    queue.append(newPath)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = deque()
        visited = set()

        stack.append([starting_vertex])

        while len(stack) > 0:
            currPath = stack.pop()
            # sets the current node to the end of the starting vertex list
            currNode = currPath[-1]

            if currNode == destination_vertex:
                return currPath
            if currNode not in visited:
                visited.add(currNode)
                for neighbor in self.vertices[currNode]:
                    newPath = list(currPath)
                    newPath.append(neighbor)
                    stack.append(newPath)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass


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
    print('graph verticies')
    print(graph.vertices)
    print('---')
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
    print('BFT')
    graph.bft(1)
    print('---')
    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('DFT')
    graph.dft(1)
    print('---')
    print('DFT recursive')
    graph.dft_recursive(1)
    print('---')
    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('BFS start 1, goal 6')
    print(graph.bfs(1, 6))
    print('---')
    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('DFS start 1, goal 6')
    print(graph.dfs(1, 6))
    print('---')
    print('DFS recursive start 1, goal 6')
    print(graph.dfs_recursive(1, 6))

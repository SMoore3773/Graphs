"""
Find the deepest node of the deepest path given a starting point. If more than one path is the same depth, return the smallest of the values
data being input is a list of tuples, where (parent, child)

verts will be the numbers representing the individuals

verts = {
    child1 = {parent1},
    child2 = {parent1, parent2},
    child3 = {parent3}
}

using the children as the vertecies will let us search the parent sets for common parents and if a parent is a child of another vertex, we can move up the family tree

DFT is going to be used, because we are not interested in finding the shortest path to the destination

traverse the graph, and add a child to a list if it has no parents that will be the list of oldest ancestors for each line in the list,

take that list of oldest ancestors, then search the list to find the paths to those ancestors, and then compare the lengths of those returned paths to find the longest of those

return the last value in the longest path, if there are more than one path with the same length, then compare the last values of those and return the smallest numeric value of those

keep track of furthest node from the starting node and return that, break ties by using the lowest value

"""
from collections import deque
from collections import defaultdict


def earliest_ancestor(ancestors, starting_node):
    graph = createGraph(ancestors)
    earliest_ancestor = (starting_node, 0)
    stack = deque()
    stack.append((starting_node, 0))
    visited = set()

    while len(stack) > 0:
        curr = stack.pop()
        currNode, distance = curr[0], curr[1]
        visited.add(curr)

        if currNode not in graph:
            if distance > earliest_ancestor[1]:
                earliest_ancestor = curr
            elif distance == earliest_ancestor[1] and currNode < earliest_ancestor[0]:
                earliest_ancestor = curr
        else:
            for ancestor in graph[currNode]:
                if ancestor not in visited:
                    stack.append((ancestor, distance + 1))
    return earliest_ancestor[0] if earliest_ancestor != starting_node else -1


def createGraph(edges):
    graph = defaultdict(set)
    for edge in edges:
        ancestor, child = edge[0], edge[1]
        graph[child].add(ancestor)
    return graph


#     # create the graph of parents and children
#     graph = {}
#     for edge in ancestors:
#         parent, child = edge[0], edge[1]

#         if child in graph:
#             graph[child].add(parent)
#         else:
#             graph[child] = {parent}
#     # edge case that starting person has no parents
#     if starting_node not in graph:
#         return -1

#     # traverse the graph to populate the list to keep track of the oldest in each lineage
#     oldest_in_line = dft(graph, starting_node)
#     print(oldest_in_line)

# def dft(graph, starting_node):
#     oldest = []
#     visited = set()
#     stack = deque()
#     stack.append(starting_node)
#     lineage = []

#     while len(stack) > 0:
#         currNode = stack.pop()
#         print('currNode in dft',currNode)
#         if currNode not in visited:
#             visited.add(currNode)
#         if currNode not in graph:
#             oldest.append(currNode)
#             for parent in graph[currNode]:

#                 stack.append(parent)
#     return oldest

ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(ancestors, 8))

#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python

import sys

# Create a graph from the input data
graph = {}
for line in sys.stdin:
    try:
        src, dst = map(int, line.strip().split())
        if src in graph:
            graph[src].append(dst)
        else:
            graph[src] = [dst]
    except ValueError:
        pass

# Define the nodes X, Y, and Z
X = 2678
Y = 1690
Z = 1765

# Define a function to compute the shortest paths from a given node
def shortest_paths(node):
    heap = [(0, node, [])]
    visited = set()
    while heap:
        (cost, current, path) = heapq.heappop(heap)
        if current not in visited:
            visited.add(current)
            path = path + [current]
            if current != node:
                yield (current, cost, path)
            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    next_cost = cost + 1
                    heapq.heappush(heap, (next_cost, neighbor, path))

# Compute the shortest paths from X, Y, and Z to every other node in the graph
x_paths = [(node, cost, path) for node, cost, path in shortest_paths(X)]
y_paths = [(node, cost, path) for node, cost, path in shortest_paths(Y)]
z_paths = [(node, cost, path) for node, cost, path in shortest_paths(Z)]

# Emit the shortest paths to X, Y, and Z
for node, cost, path in x_paths:
    print(f'{node}\tX\t{cost}\t{path}')
for node, cost, path in y_paths:
    print(f'{node}\tY\t{cost}\t{path}')
for node, cost, path in z_paths:
    print(f'{node}\tZ\t{cost}\t{path}')


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python

import sys

# Initialize variables to store the shortest paths to X, Y, and Z
x_paths = {}
y_paths = {}
z_paths = {}

# Iterate over the mapper output and update the shortest paths dictionaries
for line in sys.stdin:
    try:
        node, target, cost, path = line.strip().split('\t')
        cost = int(cost)
        path = list(map(int, path.strip('[]').split(', ')))
        if target == 'X':
            if node not in x_paths or cost < x_paths[node][0]:
                x_paths[node] = (cost, path)
        elif target == 'Y':
            if node not in y_paths or cost < y_paths[node][0]:
                y_paths[node] = (cost, path)
        elif target == 'Z':
            if node not in z_paths or cost < z_paths[node][0]:
                z_paths[node] = (cost, path)
    except ValueError:
        pass

# Print the results
for node in x_paths.keys():
    x_cost, x_path = x_paths[node]
    y_cost, y_path = y_paths.get(node, (-1, []))
    z_cost, z_path = z_paths.get(node, (-1, []))
    print(f'{node}\t{x_cost}\t{x_path}\t{y_cost}\t{y_path}\t{z_cost}\t{z_path}')


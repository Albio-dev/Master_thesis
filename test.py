import json

import constraints
import itertools
import re

with open('convert.json', 'r') as convert_file:
    test = json.loads(convert_file.read())


t1 = test['t1']

print(t1)

def make_graph(variables):
    graph = []
    for i, j in itertools.combinations(variables, 2):
        if i != j:
            graph.append((i, j))

    return graph

graph = make_graph(t1)
print(f'size: {len(graph)}\ngraph: {graph}')

constraints_manager = constraints.constraints_manager()

valid_graph = []
for index, i in enumerate(graph):
    print(f'{index}. {i}: Contained={constraints_manager.contained(x = t1[i[0]], y = t1[i[1]])} Sequence={constraints_manager.sequence(t1[i[0]], t1[i[1]])}')
    if not (constraints_manager.contained(x = t1[i[0]], y = t1[i[1]]) or constraints_manager.sequence(t1[i[0]], t1[i[1]])):
        valid_graph.append(i)

print(f'valid_graph: {valid_graph}')

def support(graph, variables):
    support = []
    for i in variables:
        for j in graph:
            if i in j:
                support.append(j)
    return support

print(support(t1, ['x1', 'x3']))

'''

variables = (constraints_manager.to_variables('t1', len(test['t1'])))
constraints =  constraints_manager.gen_constraints('t1', len(test['t1']))
'''

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from(t1.keys())
G.add_edges_from(valid_graph)

nx.draw(G, with_labels=True)
plt.show()
print(nx.algorithms.approximation.max_clique(G))
import networkx as nx
import matplotlib.pyplot as plt
import json
import itertools

import constraints
import graph_handler



with open('convert.json', 'r') as convert_file:
    test = json.loads(convert_file.read())

graphs = graph_handler.graph_handler()
G = graphs.make_subject_graphs(test)

graphs.apply_constraints(constraints.constraints_manager, G)


graphs.draw_graph()
plt.show()

# Create multigraph
G = nx.MultiGraph()

# TODO: Collapse commonly named node to multigraph

# Add nodes
for i in list(graphs.graphs.values()):
    G.add_edges_from(i.edges)
nx.draw(G, with_labels=True)

G.edges(data=True)
plt.show()
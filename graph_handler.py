import itertools
import networkx as nx
import matplotlib.pyplot as plt

import constraints

class graph_handler:

    def __init__(self, graphs = None) -> None:
        if graphs is None:
            self.graphs = {}
        else:
            self.graphs = graphs

    def make_subject_graphs(self, data):
        for i, j in data.items():
            self.graphs[i] = self.make_timeline_graph(j)

        return self.graphs

    # Fill the graph based on the data
    # Given a dictionary like this:
    # {'x1':[(1, 2), (4, 5)], 'x2':[(2, 3)]}
    # it will create a graph like this:
    # [('x1_0', {'b': 1, 'e': 2}), ('x1_1', {'b': 4, 'e': 5}), ('x2_0', {'b': 2, 'e': 3})]
    def make_timeline_graph(self, timeline):
        G = nx.Graph()

        for i, j in timeline.items(): 
            for l, k in enumerate(j):
                G.add_node(f'{i}_{l}', b=k[0], e=k[1])

        return G
    
    def apply_constraints(self, constraints_class, G = None):
        if G is None:
            G = self.graphs

        for name, graph in G.items():
            for i, j in itertools.combinations(graph.nodes(data=True), 2):
                if not any(constraints_class.check(i[1], j[1])):
                    graph.add_edge(i[0], j[0])

        return G

    def draw_graph(self, G = None):
        if G is None:
            G = self.graphs

        for name, graph in G.items():
            nx.draw(graph, with_labels=True)


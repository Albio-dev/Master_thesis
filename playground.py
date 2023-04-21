import json
import networkx as nx
import matplotlib.pyplot as plt
from graphs import graph_handler




with open('convert.json', 'r') as convert_file:
    test = json.loads(convert_file.read())


G = graph_handler.sample_to_graph(test)


test = nx.DiGraph()
test.add_node(0, class_name = 'a')
test.add_node(1, class_name = 'b')
test.add_node(2, class_name = 'c')
test.add_edge(1, 0, type='L')
test.add_edge(0, 2, type='B')
test.add_edge(1, 2, type='L')

subgraph = G.subgraph([j[0] for j in G.nodes(data=True) for i in test.nodes(data=True) if i[1]['class_name'] == j[1]['class_name']])

fig, axs = plt.subplots(1, 2)
nx.draw_networkx(subgraph, ax=axs[0], with_labels=True, labels = {i: (j['class_name'], i) for i, j in subgraph.nodes(data=True)})
nx.draw_networkx(test, ax=axs[1], with_labels=True, labels = {i: (j['class_name'], i) for i, j in test.nodes(data=True)})
fig.show()

print(graph_handler.is_present(G, test))


plt.show()
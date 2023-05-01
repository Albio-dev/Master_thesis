import matplotlib.pyplot as plt
import networkx as nx


def relationship(node1, node2):
    name1 = node1[0]
    name2 = node2[0]
    val1 = node1[1]
    val2 = node2[1]

    # Late, if a late b
    if val1[0] >= val2[1]:
        type = 'L'
        orientation = (name1, name2)
    elif val1[1] <= val2[0]:
        type = 'L'
        orientation = (name2, name1)
    
    # Before, if a before b
    elif val1[0] == val2[0] and val1[1] > val2[1]:
        type = 'B'
        orientation = (name1, name2)
    elif val1[0] == val2[0] and val1[1] < val2[1]:
        type = 'B'
        orientation = (name2, name1)

    # Early if a early b
    elif val1[0] < val2[0] and val1[1] == val2[1]:
        type = 'E'
        orientation = (name1, name2)
    elif val1[0] > val2[0] and val1[1] == val2[1]:
        type = 'E'
        orientation = (name2, name1)

    # Overlap if a overlap b
    elif val1[0] < val2[0] and val1[1] > val2[1]:
        type = 'O'
        orientation = (name1, name2)
    elif val1[0] > val2[0] and val1[1] < val2[1]:
        type = 'O'
        orientation = (name2, name1)

    # During if a during b
    elif val1[0] < val2[0] and val1[1] < val2[1]:
        type = 'D'
        orientation = (name1, name2)
    elif val1[0] > val2[0] and val1[1] > val2[1]:
        type = 'D'
        orientation = (name2, name1)
    
    return orientation, type

    
class graph_handler:

    # A single sample with multiple timelines
    def sample_to_graph(data):
        # Parse data into a graph
        G = nx.DiGraph()

        # Initialize unique ids
        id = 0

        # Iterate through each timeline
        for _, j in data.items():

            # Keep track of time index for each timeline
            last_end = 0

            # Iterate through each event
            for k in j:
                # Ignore empty events
                if k[0] is not None:
                    begin = last_end
                    end = last_end + k[1]
                    G.add_node(id, begin = begin, end = end, class_name = k[0])

                    # Iterate through all nodes to determine relationships
                    for name, value in G.nodes(data=True):
                        if name != id:

                            # Determine relationship type
                            orientation, type = relationship((id, (begin, end)), (name, (value['begin'], value['end'])))
                    
                            # Add edge
                            G.add_edge(*orientation, type=type)
                    
                    id += 1

                # Add duration to time index
                last_end += k[1]

        return G

    def draw(graph, ax = None):
        if ax is None:
            fig, ax = plt.subplots(figsize=(10, 10))
        nx.draw_networkx(graph, ax=ax, with_labels=True, labels = {i: (j['class_name'], i) for i, j in graph.nodes(data=True)})


    def is_present(text, query):
        subgraph = text.subgraph([j[0] for j in text.nodes(data=True) for i in query.nodes(data=True) if i[1]['class_name'] == j[1]['class_name']])

        def edge_eq(n1, n2):
            return n1['type'] == n2['type']
        def node_eq(n1, n2):
            return n1['class_name'] == n2['class_name']
        
        return nx.isomorphism.DiGraphMatcher(subgraph, query, node_match = node_eq, edge_match=edge_eq).subgraph_is_isomorphic()
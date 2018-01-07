import itertools

import networkx
from matplotlib import pyplot

TESTDATA = [
    ["Bi", "Ta", "Da", "Lo"],
    ["Mi", "Ry", "Ch"],
    ["Bi", "Ta", "Da"],
    ["Bi", "Ta", "Da", "Le"],
    ["Lo", "Sa", "Mi"],
    ["Ch", "Mi", "Ko"],
    ["Uu", "Lo", "Ko"],
    ["Bi", "Da", "Le"],
    ["Gr", "Da", "Ta", "Le", "Bi"],
    ["Pa", "Il", "Sh", "Hi"],
    ["Gr", "Bl", "Bi", "Da"]
]

def get_color(n):
    color_mapping = {
        "Bi": "g",
        "Ta": "b",
        "Da": "r",
        "Lo": "c",
        "Mi": "r",
        "Ry": "g",
        "Ch": "y",
        "Le": "c",
        "Sa": "r",
        "Ko": "g",
        "Uu": "c",
        "Gr": "c",
        "Bl": "b",
        "Pa": "r",
        "Il": "b",
        "Sh": "c",
        "Hi": "y",
    }
    return color_mapping[n]

def plot(data):
    graph = networkx.Graph()
    for d in data:
        graph.add_edges_from(itertools.combinations(d, 2))
    for connected_group in networkx.connected_components(graph):
        subgraph = networkx.subgraph(graph, connected_group)
        node_list, node_size = zip(*networkx.degree(subgraph))
        color_list = [get_color(n) for n in node_list]
        node_size = [200*n for n in node_size]
        print(node_size)
        pyplot.figure()
        pyplot.subplot(121)
        networkx.draw(
            subgraph,
            nodelist=node_list,
            node_size=node_size,
            node_color=color_list,
            font_size=10,
            font_color='w',
            width=.5,
            with_labels=True)
        pyplot.subplot(122)
        pyplot.axis('equal')
        networkx.draw_circular(
            subgraph,
            nodelist=node_list,
            node_size=node_size,
            node_color=color_list,
            font_size=12,
            font_color='w',
            width=.5,
            with_labels=True,)
    pyplot.show()

plot(TESTDATA)

# utils/graph_utils.py

import networkx as nx
import matplotlib.pyplot as plt


def visualize_graph(graph, folder):
    G = nx.Graph()

    # Add nodes to the graph
    for node in graph:
        G.add_node(node)

    # Add edges to the graph
    for node, node_data in graph.items():
        for relation in node_data["relations"]:
            other_node, rel = relation
            G.add_edge(node, other_node, label=rel)

    # Draw the graph
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue')
    nx.draw_networkx_labels(G, pos, font_size=12)
    nx.draw_networkx_edges(G, pos, edge_color='gray')
    labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Save the graph visualization
    output_path = f"output/{folder}_graph.png"
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(output_path, format='PNG')
    plt.close()

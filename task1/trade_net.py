import networkx as nx
import matplotlib.pyplot as plt

def gen_matrix():
    nodes = [
      "Термінал 1", "Термінал 2", 
      "Склад 1", "Склад 2", "Склад 3", "Склад 4",
      "Магазин 1", "Магазин 2", "Магазин 3", "Магазин 4", "Магазин 5",
      "Магазин 6", "Магазин 7", "Магазин 8", "Магазин 9", "Магазин 10",
      "Магазин 11", "Магазин 12", "Магазин 13", "Магазин 14"
  ]

    edges = [
      ("Термінал 1", "Склад 1", 25),
      ("Термінал 1", "Склад 2", 20),
      ("Термінал 1", "Склад 3", 15),
      ("Термінал 2", "Склад 3", 15),
      ("Термінал 2", "Склад 4", 30),
      ("Термінал 2", "Склад 2", 10),
      ("Склад 1", "Магазин 1", 15),
      ("Склад 1", "Магазин 2", 10),
      ("Склад 1", "Магазин 3", 20),
      ("Склад 2", "Магазин 4", 15),
      ("Склад 2", "Магазин 5", 10),
      ("Склад 2", "Магазин 6", 25),
      ("Склад 3", "Магазин 7", 20),
      ("Склад 3", "Магазин 8", 15),
      ("Склад 3", "Магазин 9", 10),
      ("Склад 4", "Магазин 10", 20),
      ("Склад 4", "Магазин 11", 10),
      ("Склад 4", "Магазин 12", 15),
      ("Склад 4", "Магазин 13", 5),
      ("Склад 4", "Магазин 14", 10),
  ]

    node_indices = {node: i for i, node in enumerate(nodes)}

    num_nodes = len(nodes)
    capacity_matrix = [[0] * num_nodes for _ in range(num_nodes)]

    for from_node, to_node, capacity in edges:
        i, j = node_indices[from_node], node_indices[to_node]
        capacity_matrix[i][j] = capacity

    sink_nodes = [node for node in nodes if "Магазин" in node]

    # Побудова графа з підписами потоків
    G = nx.DiGraph()
    for from_node, to_node, capacity in edges:
        G.add_edge(from_node, to_node, capacity=capacity)

    # Візуалізація графа
    pos = nx.spring_layout(G)  
    labels = {(u, v): f"{d['capacity']}" for u, v, d in G.edges(data=True)}
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=10)
    plt.show()
    return capacity_matrix, sink_nodes, node_indices



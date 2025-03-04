import pandas as pd
from edmonds_karp import edmonds_karp
from trade_net import gen_matrix

source_nodes = ["Термінал 1", "Термінал 2"]
capacity_matrix, sink_nodes, node_indices = gen_matrix()

results = []
for source in source_nodes:
    for sink in sink_nodes:
        max_flow = edmonds_karp(capacity_matrix, node_indices[source], node_indices[sink])
        results.append([source, sink, max_flow])


data_frame = pd.DataFrame(results, columns=["Термінал", "Магазин", "Фактичний Потік (одиниць)"])
print(data_frame)
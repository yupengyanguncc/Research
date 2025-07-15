import networkx as nx
import matplotlib.pyplot as plt

# 创建一个无向图
G = nx.Graph()
# 添加节点
G.add_nodes_from([0, 1, 2, 3])
# 添加边
G.add_edges_from([(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)])

# 画图
pos = nx.spring_layout(G, seed=42)  # 自动布局
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=800, edge_color='gray', font_size=16, width=2)

plt.title("Simple Undirected Graph")
plt.tight_layout()
plt.savefig("graph_example.png")  # 路径根据你的项目结构调整
plt.show()

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def compute_lambda2(G):
    L = nx.laplacian_matrix(G).todense()
    eigvals = np.linalg.eigvalsh(L)
    eigvals = np.sort(np.real(eigvals))
    return eigvals[1] if len(eigvals) > 1 else 0

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# 1. Disconnected graph
G1 = nx.Graph()
G1.add_nodes_from([0, 1, 2, 3])
G1.add_edges_from([(0, 1), (2, 3)])
lambda2_1 = compute_lambda2(G1)
nx.draw(G1, pos=nx.spring_layout(G1, seed=1), ax=axes[0], with_labels=True, node_color='skyblue', node_size=700)
axes[0].set_title(f"Disconnected ($\\lambda_2$ = {lambda2_1:.2f})")

# 2. Sparsely connected (global connected, few edges)
G2 = nx.cycle_graph(4)  # 0-1-2-3-0
lambda2_2 = compute_lambda2(G2)
nx.draw(G2, pos=nx.spring_layout(G2, seed=2), ax=axes[1], with_labels=True, node_color='lightgreen', node_size=700)
axes[1].set_title(f"Connected, sparse ($\\lambda_2$ = {lambda2_2:.2f})")

# 3. Densely connected (global connected, more edges)
G3 = nx.complete_graph(4)
lambda2_3 = compute_lambda2(G3)
nx.draw(G3, pos=nx.spring_layout(G3, seed=3), ax=axes[2], with_labels=True, node_color='salmon', node_size=700)
axes[2].set_title(f"Connected, dense ($\\lambda_2$ = {lambda2_3:.2f})")

for ax in axes:
    ax.axis('off')

plt.tight_layout()
plt.savefig('lambda2_graphs.png')  # 路径可根据你的项目结构调整
plt.show()
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

pubs = ["Паб Лісопилка", "Театр Пива Правда", "Пивна Дума", "Старий Лев", "Портер Паб", "Пивний Сад", "Пивна Бочка"]
G.add_nodes_from(pubs)

routes = [
    ("Паб Лісопилка", "Театр Пива Правда"),
    ("Паб Лісопилка", "Пивна Дума"),
    ("Театр Пива Правда", "Пивна Дума"),
    ("Театр Пива Правда", "Старий Лев"),
    ("Пивна Дума", "Портер Паб"),
    ("Старий Лев", "Портер Паб"),
    ("Старий Лев", "Пивний Сад"),
    ("Портер Паб", "Пивний Сад"),
    ("Портер Паб", "Пивна Бочка"),
    ("Пивний Сад", "Пивна Бочка")
]
G.add_edges_from(routes)

def dfs(graph, start):
    visited = set()
    stack = [start]
    path = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            stack.extend(reversed(list(graph[vertex])))

    return path

def bfs(graph, start):
    visited = set()
    queue = [start]
    path = []

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            queue.extend(list(graph[vertex]))

    return path

start_node = "Паб Лісопилка"

dfs_path = dfs(G, start_node)
bfs_path = bfs(G, start_node)

print("DFS Path:", dfs_path)
print("BFS Path:", bfs_path)

pos = nx.spring_layout(G)

plt.figure(figsize=(10, 5))

plt.subplot(121)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=10, font_weight="bold")
nx.draw_networkx_edges(G, pos, edgelist=list(zip(dfs_path, dfs_path[1:])), edge_color="r", width=2)
plt.title("Шлях DFS")

plt.subplot(122)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=10, font_weight="bold")
nx.draw_networkx_edges(G, pos, edgelist=list(zip(bfs_path, bfs_path[1:])), edge_color="g", width=2)
plt.title("Шлях BFS")

plt.show()

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_of_nodes = dict(G.degree())

print("Кількість вершин:", num_nodes)
print("Кількість ребер:", num_edges)
print("Ступінь вершин:")
for node, degree in degree_of_nodes.items():
    print(f"Вершина {node}: {degree}")
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

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=10, font_weight="bold")
plt.title("Туристична мапа пивних закладів Києва")
plt.show()

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_of_nodes = dict(G.degree())

print("Кількість вершин:", num_nodes)
print("Кількість ребер:", num_edges)
print("Ступінь вершин:")
for node, degree in degree_of_nodes.items():
    print(f"Вершина {node}: {degree}")

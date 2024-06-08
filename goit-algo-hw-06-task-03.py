import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

pubs = ["Паб Лісопилка", "Театр Пива Правда", "Пивна Дума", "Старий Лев", "Портер Паб", "Пивний Сад", "Пивна Бочка"]
G.add_nodes_from(pubs)

routes = [
    ("Паб Лісопилка", "Театр Пива Правда", 4),
    ("Паб Лісопилка", "Пивна Дума", 2),
    ("Театр Пива Правда", "Пивна Дума", 5),
    ("Театр Пива Правда", "Старий Лев", 10),
    ("Пивна Дума", "Портер Паб", 3),
    ("Старий Лев", "Портер Паб", 4),
    ("Старий Лев", "Пивний Сад", 11),
    ("Портер Паб", "Пивний Сад", 6),
    ("Портер Паб", "Пивна Бочка", 7),
    ("Пивний Сад", "Пивна Бочка", 1)
]
G.add_weighted_edges_from(routes)

def dijkstra(graph, start):
    shortest_paths = {start: (None, 0)}
    current_node = start
    visited = set()

    while current_node is not None:
        visited.add(current_node)
        destinations = graph[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node, data in destinations.items():
            weight = data['weight'] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return shortest_paths
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    return shortest_paths

all_shortest_paths = {}
for node in G.nodes:
    all_shortest_paths[node] = dijkstra(G, node)

pos = nx.spring_layout(G)
plt.figure(figsize=(10, 7))
nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=10, font_weight="bold")
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Граф пивних закладів Києва з вагами ребер")
plt.show()

for start_node, paths in all_shortest_paths.items():
    print(f"Найкоротші шляхи від {start_node}:")
    for end_node, (prev_node, weight) in paths.items():
        if prev_node is not None:
            print(f"  До {end_node}: вага {weight}")
    print()


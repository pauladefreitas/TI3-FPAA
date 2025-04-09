import matplotlib.pyplot as plt
import networkx as nx

def hamiltonian(graph, current, path, visited):
    if len(path) == len(graph):
        return path

    for node in sorted(graph[current]):
        if node not in visited:
            path.append(node)
            visited.add(node)

            result = hamiltonian(graph, node, path, visited)
            if result:
                return result
            path.pop()
            visited.remove(node)

    return None

def plot_graph(graph_dict, oriented, hamiltonian_path=None):
    G = nx.DiGraph() if oriented else nx.Graph()

    for node, neighbors in graph_dict.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G, seed=42)
    edge_colors = []

    hamiltonian_edges = set()
    if hamiltonian_path:
        for i in range(len(hamiltonian_path) - 1):
            u, v = hamiltonian_path[i], hamiltonian_path[i + 1]
            hamiltonian_edges.add((u, v))

    for edge in G.edges():
        if edge in hamiltonian_edges or (not oriented and (edge[1], edge[0]) in hamiltonian_edges):
            edge_colors.append('red')
        else:
            edge_colors.append('yellow')

    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color=edge_colors,
            node_size=1500, font_size=16, arrows=oriented)
    plt.title("Grafo com caminho hamiltoniano (arestas vermelhas)")
    plt.show()

def main():
    a = input("Seu grafo é orientado? (sim/não): ").strip().lower()
    oriented = True if a == "sim" else False

    n = int(input("Digite o número de vértices: "))
    m = int(input("Digite o número de arestas: "))

    graph = {i: [] for i in range(n)}

    print("Digite as arestas (dois números por linha, separados por espaço):")
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        if not oriented:
            graph[v].append(u)

    begin = int(input("Vértice inicial: "))
    path = [begin]
    visited = {begin}

    plot_graph(graph, oriented)
    result = hamiltonian(graph, begin, path, visited)
    if result:
        print("Caminho hamiltoniano encontrado:", result)
    else:
        print("Nenhum caminho hamiltoniano encontrado.")

main()
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

def plot_graph(graph_dict, oriented):
    if oriented:
        G = nx.DiGraph()
    else:
        G = nx.Graph()

    for node, neighbors in graph_dict.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=1500, font_size=16)
    plt.title("Grafo")
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

    plot_graph(graph, oriented)

    begin = int(input("Vértice inicial: "))
    path = [begin]
    visited = {begin}

    result = hamiltonian(graph, begin, path, visited)
    if result:
        print("Caminho hamiltoniano encontrado:", result)
    else:
        print("Nenhum caminho hamiltoniano encontrado.")

main()
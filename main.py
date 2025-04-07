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

    result = hamiltonian(graph, begin, path, visited)
    if result:
        print("Caminho hamiltoniano encontrado:", result)
    else:
        print("Nenhum caminho hamiltoniano encontrado.")

main()
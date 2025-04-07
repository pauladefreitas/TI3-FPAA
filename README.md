# Implementação do Algoritmo para Caminho Hamiltoniano em Python

Um caminho hamiltoniano em um grafo é um caminho que visita cada vértice exatamente uma vez. Encontrar esse caminho é um problema clássico em teoria dos grafos e está associado a problemas de alta complexidade computacional, como o Problema do Caixeiro Viajante. Este projeto tem como objetivo implementar uma abordagem para determinar se um caminho hamiltoniano existe em um grafo e, em caso afirmativo, encontrá-lo.

## Implementação do Algoritmo

A implementação inicia-se com a declaração da função recursiva principal do algoritmo.

```python
   def hamiltonian(graph, current, path, visited):
```

A partir disso, há uma condição de parada. Caso o tamanho do caminho for igual ao tamanho do grafo, o algoritmo retorna o caminho traçado.

```python
    if len(path) == len(graph):
        return path
```

Caso não entre nessa condição, o algoritmo continua sua execução, iniciando uma repetição dentro do grafo. O método _sorted()_ garante que os vizinhos sejam explorados em forma crescente, de modo que o algoritmo sempre tentará retornar o _menor_ caminho hamiltoniano primeiro.

```python
    for node in sorted(graph[current]):
```

Dentro da repetição, ocorre a validação. Se o nó analisado ainda não foi visitado, ele é adicionado ao caminho e à lista de nós visitados.

```python
    if node not in visited:
        path.append(node)
        visited.add(node)
```

Após a validação, se o nó não for visitado, há a variável _result_, que faz uma chamada recursiva no método.

```python
    result = hamiltonian(graph, node, path, visited)
```

Caso houver resultado, ele é retornado. Caso não haja resultado, entra o _backtracking_.

No caso de um resultado não ser retornado, significa que a recursão finalizou e nenhum caminho hamiltoniano foi encontrado. Neste caso, o _backtracking_ entra em ação, removendo o último vértice adicionado à lista _path_ e remove o nó (ou vértice) do conjunto de visitados.

Assim, novos caminhos podem ser testados.

```python
    path.pop()            #remove o último nó adicionado a path
    visited.remove(node)  #remove o último nó adicionado ao conjunto de visitados
```

## Como rodar em ambiente local?

### Passo 1: Clonar o repositório

1. Clone o repositório git em uma pasta no seu ambiente local com o seguinte comando:

   ```bash
   git clone https://github.com/pauladefreitas/TI3-FPAA.git
   cd TI3-FPAA
   ```

### Passo 2: Executar o script

1. Execute o script principal:

   ```bash
   python main.py
   ```

2. O programa questionará se o grafo a ser traçado um caminho hamiltoniano é orientado ou não.

   ```bash
   Seu grafo é orientado? (sim/não):
   ```

3. Após isso, é pedido número de vértices e número de arestas.

   ```bash
   Digite o número de vértices:
   Digite o número de arestas:
   ```

4. Depois, é pedido que o usuário digite o valor das arestas.

   ```bash
   Digite as arestas (dois números por linha, separados por espaço):
   ```

5. Por fim, é requisitado qual será o vértice inicial.

   ```bash
   Vértice inicial:
   ```

6. O resultado será exibido logo depois.

## Relatório Técnico

### Análise da complexidade computacional

As classes P, NP, NP-Completo e NP-Difícil são categorias utilizadas na ciência da computação teórica para classificar problemas de acordo com a dificuldade de resolvê-los ou verificar suas soluções.

1. O problema do caminho hamiltoniano se enquadra na classe NP-Completo.

2. A classe NP foca em problemas cujas soluções podem ser verificadas rapidamente, ainda que encontrar a solução não seja necessariamente rápido. Os problemas NP-Completo representam os desafios mais difíceis dentro de NP, sendo que resolver um deles eficientemente significaria resolver todos os outros problemas de NP da mesma forma.

### Análise da complexidade assintótica de tempo

1. A complexidade é O(n!), onde n é o número de vértices.

2. Método: Contagem de operações e análise combinatória.
   O algoritmo tenta todas as permutações possíveis de vértices.

Cada permutação representa um caminho potencial.

Como existem n! permutações possíveis, e cada uma exige verificação (se os vértices são conectados), o tempo de execução cresce como O(n!).

### Teorema Mestre

- É possível aplicar?

Não.

Justificativa:
O Teorema Mestre é usado para resolver recorrências do tipo divide-and-conquer, como:

T(n)=a⋅T(n/b)+f(n)
O algoritmo de Caminho Hamiltoniano não divide o problema em subproblemas menores do mesmo tipo.

Ele usa backtracking puro, o que leva a uma recorrência não uniforme baseada em ramificações, e não em divisões regulares.

Portanto, o Teorema Mestre não se aplica.

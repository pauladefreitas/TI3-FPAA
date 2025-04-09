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

As classes P, NP, NP-Completo e NP-Difícil são categorias utilizadas na ciência da computação teórica para classificar problemas de acordo com a dificuldade de resolvê-los ou verificar suas soluções. Ou seja, para estudo teórico da complexidade de algoritmos, considera-se problemas cujo resultado da computação seja sim ou não.

1. O problema do caminho hamiltoniano se enquadra na classe NP-Completo.

2. A classe 𝑁𝑃 contém problemas de decisão cujas soluções podem ser verificadas em tempo polinomial `O(n^k)` por um algoritmo determinístico.

Os problemas 𝑁𝑃-Completos são um subconjunto de 𝑁𝑃 com duas características principais: pertencem à classe 𝑁𝑃, ou seja, suas soluções podem ser verificadas em tempo polinomial e são 𝑁𝑃-Difíceis, o que significa que todo problema em 𝑁𝑃 pode ser reduzido a eles em tempo polinomial.

Um problema é NP-completo se ele é tanto NP como NP-difícil. Em outras palavras, um problema NP-completo é um problema em NP para o qual se pode mostrar que todos os problemas em NP podem ser reduzidos a ele em tempo polinomial. Resolver qualquer problema NP-completo eficientemente implicaria em resolver eficientemente todos os problemas em NP e, portanto, P seria igual a NP.

Sendo assim, encontrando uma solução para o problema do caminho hamiltoniano, encontra-se, também, uma solução para o problema do caixeiro viajante, visto que qualquer problema em 𝑁𝑃 pode ser reduzido a ele. O problema do caixeiro viajante encontra um caminho eficiente que percorre um conjunto de cidades exatamente uma vez, retornando ao ponto de partida, com o menor custo total possível. Como sua versão de decisão é NP-completa, uma solução polinomial para esse problema também resolveria, indiretamente, todos os outros problemas em NP, evidenciando a importância desse problema no estudo da complexidade computacional.

### Análise da complexidade assintótica de tempo

1. A complexidade é O(n!), onde n é o número de vértices.

2. O algoritmo explora todas as 𝑛! permutações possíveis das 𝑛 vértices. Para cada permutação, ele calcula o custo total do percurso, resultando em 𝑛! operações principais. Essa análise é baseada na contagem de operações, pois o número de permutações domina o comportamento do algoritmo.

### Teorema Mestre

O Teorema Mestre não é aplicável neste caso.

O **Teorema Mestre** é uma ferramenta para resolver **recorrências de algoritmos recursivos**, esse tipo de recorrência aparece em **algoritmos divide-and-conquer**.

Onde:
- `a` é o número de subproblemas;
- `b` é o tamanho de cada subproblema;
- `f(n)` é o custo de combinar os resultados.

2. O algoritmo utilizado para encontrar um caminho Hamiltoniano é um **backtracking** puro, com as seguintes características: ele não divide o problema em subproblemas de tamanho n/b, ele **explora todas as combinações possíveis de caminhos** e sua recorrência não segue o padrão necessário para aplicar o Teorema Mestre.

A recorrência associada é mais parecida com:

$$
T(n) = n \cdot T(n - 1)
$$

Ou seja, ela representa a **permutação dos vértices**, e resulta em complexidade `O(n!)`, que cresce muito mais rápido do que qualquer função polinomial ou mesmo exponencial do tipo `aT(n/b)`.

### Análise dos casos de complexidade

1. 
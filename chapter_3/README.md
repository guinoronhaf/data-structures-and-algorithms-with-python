# Técnicas de _design_ de algoritmos

Compreender as técnicas de design de algoritmos é fundamental para entender melhor os problemas e produzir algoritmos mais sofisticados, aplicando o design certo para determinados tipos de problemas.

As principais técnicas de _desing_ abordadas aqui são:

 - [Divisão e Conquista](#divisão-e-conquista)
 - [Programação dinâmica](#programação-dinâmica)
 - [Algoritmos gananciosos](#algoritmos-gananciosos)

## Divisão e conquista

## Programação dinâmica

Em programação dinâmica, a principal ideia é **evitar recálculo de valores após a divisão do problema em subproblemas menores**. Aplica-se, então, a técnica de _memoização_. De modo geral, resultados intermediários são guardados em algum tipo de _cache_ (como Array ou tabela Hash).

Ao contrário da abordagem de divisão e conquista, em que os problemas menores (subproblemas) são independentes, aqui eles estão interligados, em sobreposição. Dessa forma, faz sentido armazenar valores já calculados, uma vez que eles provavelmente serão consultados depois.

### Sequência de Fibonacci

A sequência de Fibonacci é um bom exemplo. Consideremos a implementação recursiva básica:

```python
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
```

Tem-se aqui que o valor de _fib(3)_, por exemplo, tem que ser calculado _duas vezes_. Não seria melhor armazenas esse valor? Essa necessidade fica mais evidente ao perceber que podemos representar o algoritmo acima como uma árvore binária, em que sempre acessamos os dois ramos. Isso resulta em uma ordem de complexidade péssima de $`O(2^{n})`$.

Vamos agora representar isso com prog. dinâmica:

```python
def fib(n):
    global lookup
    if n == 0:
        return 0
    if n == 1:
        return 1
    if lookup[n] is not None: #array atuando como cache
        return lookup[n]
    lookup[n] = fib(n - 1) + fib(n - 2) #memoizando valor (adicionando-o ao cache)
    return lookup[n]


lookup = [None] * 1000

for i in range(6):
    print(fib(i))
```

Após essa mudança, temos que, no pior caso, teremos que fazer o cálculo pelo menos uma vez para cada um dos _n_ elementos em _fib(n)_. Assim, a complexidade se torna _O(n)_.

## Algoritmos gananciosos

Em geral, algoritmos ganaciosos são aqueles em que seleciona-se a melhor opção possível (solução ótima) a cada etapa de execução do algoritmo. Dessa forma, é bastante provável que, ao final da execução, considerando as **soluções ótimas locais**, obtenha-se uma **solução ótima global**, ou algo próximo disso.

O **algoritmo de menor caminho de Dijkstra** é um bom exemplo de algoritmo ganacioso. A cada etapa, seleciona-se o menor caminho para determinado nó/vértice de um grafo.

Um exemplo clássico é o da **mochila com pesos**, em que deve-se maximizar o valor dos elementos dentro de uma mochila, respeitando certo limite de peso.

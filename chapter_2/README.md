## Análise de desempenho de algoritmos

Um algoritmo é considerado ótimo se ele devolve a saída esperada (conforme a entrada requerida) dentro das restrições de tempo de execução e consumo de memória auxiliar. Uma das forma de analisar o tempo de execução, medida bastante importante, é observar a complexidade desse fator.

### Análise de tempo de execução

A análise de complexidade de tempo de execução pode ser feita de diversas formas, seja limitando a função que descreve o algoritmo superiormente, inferiormente ou de ambas as formas. Cada uma dessas abordagens é expressa a seguir:

#### Notação _theta_ ($`\theta`$)

A notação _theta_ busca fornecer um limite restrito para a função que descreve o tempo de execução do algoritmo, limitando-a superior e inferiormente. Assim, sendo _T(n)_ a função que descreve o tempo de execução do algoritmo e _F(n)_, a função de _n_ tal que $`T(n) = \theta(F(n))`$, tem-se que:

$`0 \leq c_1.(F(n)) \leq T(n) \leq c_2.(F(n)), n \geq n_0`$

#### Notação _Big O_

A notação _Big O_ permite identificar um limite superior para a função que descreve o tempo de execução do algoritmo, de modo que, no pior caso, o tempo de execução daquele programa, esteja dentro daquela classe de complexidade. Vale ressaltar que a notação _O(n³)_, por exemplo, é um conjunto de funções polinomiais cujos graus são menores ou iguais a **3**. Sendo, portanto, _T(n)_ a função que descreve o tempo de execução do algoritmo e _F(n)_, a função de _n_ tal que _T(n) = O(F(n))_, tem-se:

$`T(n) \leq c.F(n), n \geq n_0`$

##### Exercícios

**1) Encontre o limite superior da função $`T(n) = 2n + 7`$**.

$`T(n) = 2n + 7`$

$`F(n) = n`$

Tem-se, então, que:

$`T(n) <= c.F(n),  n >= n_0`$

$`2n + 7 <= c.n,  n >= n_0`$

Divindo ambos os termos por _n_:

$`2 + \frac{7}{n} <= c,  n >= n_0`$

Como, para _n_ >= 1, o valor máximo de:

$`2 + \frac{7}{n}`$ é **9**, então:

$`c = 9`$ e $`n_0 = 1`$

Portanto:

$`T(n) = O(n)`$

**2) Encontre o limite superior da função $`T(n) = 2n + 5`$**.

$`T(n) = 2n + 5`$

$`F(n) = n`$

Tem-se, então, que:

$`T(n) <= c.F(n), para n >= n_0`$

$`2n + 5 <= c.n, para n >= n_0`$

Assim, como:

$`2n + 5 <= 3n, para n >= 5`$

Tem-se:

$`c = 3`$ e $`n_0 = 5`$

Portanto:

$`T(n) = O(n)`$

**3) Encontre $`F(n)`$ para a função $`T(n) = n² + n`$, tal que $`T(n) = O(F(n))`$.**

$`T(n) = n² + n`$

Por análise assintótica, sabe-se que, conforme _n_ aumenta consideralvemente:

$`n² + n \approx n²`$

Assim:

$`F(n) = n²`$

Tem-se, então, que:

$`n² + n <= c.n², para n >= n_0`$

$`n² + n <= 2n², para n >= n_0`$

Assim:

$`c = 2`$

$`n_0 = 1`$

Portanto:

$`T(n) = O(F(n)) = O(n²)`$

**4) Prove que $`F(n) = 2n³ - 6n \neq O(n²)`$.**

Aqui, não se pode provar apenas que é _O(n³)_, já que _O(n³)_ inclui as funções de grau superior ou igual a ela.

Portanto, deve-se demonstrar que $`F(n) \neq O(n²)`$

Note que:

$`F(n) = 2n³ - 6n \geq n², \forall n \geq 1`$

Portanto:

$`F(n) \neq O(n²)`$

**5) Prove que $`20n² + 2n + 5 = O(n²)`$.**

$`T(n) = 20n² + 2n + 5`$

$`F(n) = n²`$

Tem-se que:

$`20n² + 2n + 5 \leq c.n², n \geq n_0`$

Note que:

$`20n² + 2n + 5 \leq 20n² + n², n \geq 4`$, pois $`2n + 5 \leq n², n \geq 4`$

$`20n² + 2n + 5 \leq 21n², n \geq 4`$

Assim:

$`c = 21`$

$`n_0 = 4`$

E:

$`T(n) = 20n² + 2n + 5 = O(F(n)) = O(n²)`$

#### Notação _ômega_ ($`\Omega`$)

A notação ômega representa um limite de inferior, isto é, expõe o melhor caso do algoritmo. A ideia de conjunto para notações $`\Omega(n³)`$, por exemplo, continuam valendo como na notação _Big O_. Assim, sendo _T(n)_ a função que representa o tempo de execução do algoritmo e _F(n)_ sua classe de complexidade na notação _ômega_, tem-se que:

$`c.(F(n)) \leq T(n), n \geq n_0`$

##### Exercícios

**1) Encontre _F(n)_ para a função $`T(n) = 2n² + 3`$ tal que $`T(n) = \Omega(F(n))`$.**

$`T(n) = 2n² + 3`$

$`F(n) = n²`$

Assim:

$`0 \leq c.n² \leq 2n² + 3, n \geq n_0`$

$`0 \leq 2n² \leq 2n² + 3, n \geq 1`$

Então:

$`c = 2`$

$`n_0 = 1`$

Portanto:

$`T(n) 2n² + 3 = \Omega(F(n)) = \Omega(n²)`$

**2) Encontre o limite inferior para _T(n) = 3n²_.**

$`T(n) = 3n²`$

$`F(n) = n²`$

Tem-se que:

$`0 \leq c.n² \leq 3n², n \geq n_0`$

$`0 \leq n² \leq 3n², n \geq 0`$

Assim:

$`c = 1`$

$`n_0 = 0`$

Portanto:

$`T(n) = \Omega(F(n)) = \Omega(n²)`$

**3) Prove que $`3n = \Omega(n)`$.**

$`T(n) = 3n`$

$`F(n) = n`$

Tem-se que:

$`c.n \leq 3n, n \geq n_0`$

$`1.n \leq 3n, n \geq 0`$, pois $`1 \lt 3`$

Assim:

$`c = 1`$

$`n_0 = 0`$

Portanto:

$`T(n) = \Omega(F(n)) = \Omega(n)`$

### Cálculo de complexidade de tempo de execução de algoritmos

Nem sempre é possível obter as complexidades dos casos melhor e médio. No entanto, é sempre bom conhecer a ordem de complexidade de pior caso, isto é, com a notação _Big O_.

#### Exercícios

**1) Encontre a complexidade de tempo de execução do pior caso do trecho de código Python a seguir:**

```python
# o loop será executado n vezes
for i in range(n):
    print("data") # tempo constante
```

Como se trata de um loop, tem-se:

$`T(n) = O(n).O(1) = O(n)`$

**2) Encontra a complexidade de tempo do trecho de código Python a seguir:**

```python
for i in range(n):
    for j in range(n): # Esse loop também será executado n vezes
        print("run")
```

Tem-se aqui loops aninhados:

$`T(n) = O(n).O(n).O(1) = O(n.n) = O(n²)`$

**3) Encontre a complexidade de tempo do trecho de código Pyhton a seguir:**

```python
for i in range(n):
    for j in range(n):
        print("run fun")
        break
```

Percebe-se que aqui há um comando _break_. Isso indica que o comando _print_ do laço mais interno será invocado apenas **uma vez**.

Tem-se, portanto:

$`T(n) = O(n).O(1).O(1) = O(n)`$

**4) Encontre a complexidade do trecho de código Python a seguir:**

```python
def fun(n):
    for i in range(n):
        print("data") # tempo constante
    # o loop mais externo será executado n vezes
    for i in range(n):
        for j in range(n): # o loop mais interno será executado n vezes
            print("run fun") # tempo constante
```

Primeiro loop:

$`T'(n) = O(n).O(1) = O(n)`$

Loops restantes:

$`T''(n) = O(n).O(n).O(1) = O(n.n) = O(n²)`$

Portanto:

$`T(n) = T'(n) + T''(n) = O(n) + O(n²) = O(n²)`$

**5) Encontre a complexidade de tempo deste trecho de código Pyhton:**

```python
if n == 0: # tempo constante
    print("data")
else:
    for i in range(n):
        print("structure")
```

Aqui, há um caso de desvio de código. O primeiro caso _if_ leva a operações primitivas, de ordem de complexidade _O(1)_. Como estamos levando em consideração o pior caso, vamos ao _else_, em que há um loop explícito.

Assim:

$`T(n) = O(n).O(1) = O(n)`$

**6) Encontre a complexidade do trecho de código Python a seguir:**

```python
i = 1 # tempo constante
j = 0 # tempo constante
while i*i < n:
    j = j + 1 # tempo constante
    i = i + 1 # tempo constante
    print("data") # tempo constante
```

Vamos considerar alguns casos aqui:

$`n = 5 \rightarrow 2 iteraçoes`$

$`n = 10 \rightarrow 3 iteraçoes`$

$`n = 20 \rightarrow 4 iteraçoes`$

Perceba que, pela condição do loop _while_, tem-se:

$`i² \lt n \leftrightarrow i \lt \sqrt{n}`$

Sendo _i_ a quantidade de iterações, segue que:

$`T(n) = O(\sqrt{n})`$

**7) Encontre a complexidade deste trecho de código Python:**

```python
i = 0
for i in range(int(n/2), n):
    j = 1
    while j + n/2 <= n:
        k = 1
        while k < n:
            k *= 2
            print("data")
            j += 1
```

Em primeiro lugar, é importante perceber que o loop mais externo, é executado $`\frac{n}{2}`$ vezes. Ou seja:

$`T'(n) = O(\frac{n}{2}) = O(n)`$

Mais adiante, tem-se o primeiro loop _while_, em que:

$`j + \frac{n}{2} \leq n \leftrightarrow j \leq \frac{n}{2}`$

$`T''(n) = O(\frac{n}{2}) = O(n)`$

Por fim, _k_ parte de 1 até _n_, sendo dobrado a cada iteração:

$`T'''(n) = O(\log_{2}{n})`$

Portanto, como os laços são aninhados:

$`T(n) = T'(n).T''(n).T'''(n)`$

$`T(n) = O(n).O(n).O(\log_{2}{n})`$

$`T(n) = O(n.n.\log_{2}{n}) = O(n²\log_{2}{n})`$

### Exercícios finais do capítulo

**1) Encontra a complexidade dos trechos de código python a seguir:**

**a)**

```python
i = 1
while i < n:
    i *= 2
    print("data")
```

Note que:

 - Para _n_ = 5, tem-se **3** iterações;
 - Para _n_ = 10, tem-se **4** iterações;
 - Para _n_ = 20, tem-se **5** iterações.

Assim, tem-se que a cada vez que o tamanho da entrada _n_ é duplicado, o número _i_ de iterações aumenta em **uma** unidade.

Dessa forma, assumindo que o _loop_ possui _k_ iterações, tem-se que:

$`n \approx 2^{k} \leftrightarrow k \approx \log_{2}{n}`$

Portanto:

$`T(n) = O(\log_n{2}{n})`$

**b)**

```python
i = n
while i > 0:
    print("complexity")
    i /= 2
```

Note que:

 - Para _n_ = 5, tem-se **3** iterações
 - Para _n_ = 10, tem-se  **4** iterações
 - Para _n_ = 20, tem-se **5** iterações

Da mesma forma, tem-se que a cada vez que o tamanho da entrada _n_ é duplicado, o número _i_ de iterações aumenta em **uma** unidade.

$`n \approx 2^{k} \leftrightarrow k \approx \log_{2}{n}`$

Portanto:

$`T(n) = O(\log_n{2}{n})`$

**c)**

```python
for i in range(1, n):
    j = i
    while j < n:
        j *= 2
```

Analisando complexidade do laço mais externo:

$`T'(n) = O(n)`$

Analisando complexidade do laço mais interno:

$`T''(n) = \log_n{2}{n} + (\log_n{2}{n} - 1) + (\log_n{2}{n} - 2) + ... + 1`$

$`= \frac{\log_{2}{n}.(\log_{2}{n} + 1)}{2} \approx (\log_{2}{n})²`$

$`T''(n) = O((\log_{2}{n})²)

Sendo os laços aninhados:

$`T(n) = T'(n).T''(n)`$ = O(n).O((\log_{2}{n})²) = O(n.(\log_{2}{n})²)`$

**d)**

```python
i = 1
while i < n:
    print("python")
    i = i ** 2
```

Note que:

 - Para _n_ = 5, tem-se **2** iterações
 - Para _n_ = 10, tem-se **2** iterações
 - Para _n_ = 20, tem-se **3** iterações
 - Para _n_ = 40, tem-se **5** iterações

Livro meio confuso nas letras c) e d).

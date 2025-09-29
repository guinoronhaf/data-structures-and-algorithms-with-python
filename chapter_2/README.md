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

$`1.n \leq 3n, n \geq 0`$, pois $`1 \l 3`$

Assim:

$`c = 1`$

$`n_0 = 0`$

Portanto:

$`T(n) = \Omega(F(n)) = \Omega(n)`$

## Análise de desempenho de algoritmos

### Análise de tempo de execução

#### Notação theta

#### Notação Big O

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

**4) Prove que $`F(n) = 2n³ - 6n \neq O(n²)`$.








## Análise de desempenho de algoritmos

### Análise de tempo de execução

#### Notação theta

#### Notação Big O

**1) Encontre o limite superior da função `$T(n) = 2n + 7$`**

$`T(n) = 2n + 7`$

$`F(n) = n`$

Tem-se, então que:

$`T(n) <= c.F(n), n >= n0`$

$`2n + 7 <= c.n, n >= n0`$

Divindo ambos os termos por _n_:

$`2 + \frac{7}{n} <= c, n >= n0`$

Como, para _n_ >= 1, o valor máximo de:

$`2 + \frac{7}{n}`$ é 9, então:

$`c = 9`$

Portanto:

$`T(n) = O(n)`$

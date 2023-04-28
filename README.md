# **Integral Python**
 Dois programinhas que fazem a integral de equações utilizando a Regra do Trapézio

## **Regra do Trapézio**
 Em cálculo, a regra do trapézio é uma técnica para aproximar integrais definidas. 

Ela funciona aproximando a região do gráfico de uma função f(x) como um trapézio e então calcula a sua área. Ela é definida da seguinte maneira:

### $\int\limits_a^b f(x)dx \approx (b-a)*\frac{1}{2} (f(a)+f(b))$

A regra do trapézio pode ser vista como o resultado obtido pela média da soma de Riemann da direita e da esquerda, as vezes sendo definida como isso. A integral pode ter uma aproximação ainda melhor pela partição de intervalos de integração, aplicando a regra do trapézio para cada subintervalo e então somando os resultados.

Na prática, essa forma "composta" da regra do trapézio é usualmente o que é entendido quando falamos que vamos "integrar utilizando a regra do trapézio".

Seja ${x_k}$ uma partição de $[a, b]$ tal que $a = x_0 < x_1 < \dots < x_{N-1} < x_N = b$ e $\Delta x_k$ sendo o tamanho do k-ésimo subintervalo (que é, $\Delta x_k = x_k - x_{k-1}$), então:

### $\int\limits_a^b f(x)dx \approx \sum_{k=1}^N \frac{f(x_{k-1})+f(x_k)}{2}\Delta x_k$

Quando as partições tem espaços regulares, que é normalmente o caso, ou seja, quando todo $\Delta x_k$ tem o mesmo valor $\Delta x_k$, a fórmula pode ser simplificada para eficiência de cálculo fatorando $\Delta x_k$ fora:
### $\int\limits_a^b f(x)dx \approx \frac{\Delta x}{2}(f(x_0)+2f(x_2)+2f(x_3)+2f(x_4)+\dots+2f(x_{N-1})+f(x_N))$
A aproximação fica mais precisa à medida que o número de partições aumenta (então, quanto maior o $N$, todo $\Delta x_k$ diminui). Como vamos ver abaixo, é possível que seja colocado o erro esperado na precisão do valor da integral definida, usando a regra do trapézio.
# Estudo do Problema de Dirichlet para a Equação de Poisson com Discretização Finita

Este repositório trata do problema de Dirichlet para a equação de Poisson, que é discretizado em um quadrado unitário utilizando o método de diferenças finitas com espaçamento $h = \frac{1}{N}$. As equações que descrevem $U_{mn}$, juntamente com as condições de contorno, são organizadas em um sistema linear. Esse sistema é então resolvido utilizando uma ordenação lexicográfica para facilitar o processo de solução numérica.

## Descrição do Problema 📝

A Equação de Poisson que estamos resolvendo é dada por:

```math
-\Delta u(x, y) = f(x, y), \quad (x, y) \in \Omega
```

onde $\Omega = (0, 1) \times (0, 1)$ e as condições de Dirichlet são aplicadas na fronteira $\partial\Omega$.

## Ferramentas Utilizadas 🔧

Para implementar e resolver o problema, usamos as seguintes bibliotecas Python:

- **Numpy**: Para manipulação de arrays e matrizes.
- **Scipy**: Para métodos iterativos e armazenamento de matriz esparsa.
- **Matplotlib**: Para visualização gráfica das soluções.
- **Pandas, PrettyTable e Tabulate**: Para organizar e imprimir os erros em tabelas.

## Metodologia 💻

1. **Discretização**: Utilizamos o método de diferenças finitas centradas.
2. **Resolução do Sistema Linear**: Aplicamos um método iterativo para resolver o sistema linear resultante da discretização.
3. **Simulações**: Realizamos simulações para diferentes valores de $N$ (tamanho da malha).

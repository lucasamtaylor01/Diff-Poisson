# Exercício Programa I

Este projeto é parte da disciplina **Métodos Numéricos em Equações Diferenciais II** e tem como foco a resolução numérica da **Equação de Poisson** no quadrado unitário utilizando o método de diferenças finitas.

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

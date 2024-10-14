## Exercício 2

Iniciamos definindo $u_{exata}$ e $f$ para o problema.

```python
u = lambda x,y: np.cos(x) * np.sin(y)
f = lambda x,y: -2 * np.cos(x) * np.sin(y)
```

Vamos partir da análise de funções que serão usadas na resolução dos itens (b) e (c).

O sistema que retorna $A$ e $b$ segue o mesmo que foi mencionado para o exercício 1. Desse modo para avaliarmos o erro, faremos uso da seguinte função:

```py

# Função que calcula o erro das soluções
def error_function(N, exact, numeric) -> pd.DataFrame:
    x = np.linspace(0, 1, N+1)
    y = np.linspace(0, 1, N+1)
    X, Y = np.meshgrid(x, y)

    # Solução exata nos pontos da grade
    U_exata = exact(X, Y)

    # Inserir solução numérica nos pontos internos
    U_numerica = np.zeros((N+1, N+1))
    U_numerica[1:N, 1:N] = numeric.reshape((N-1, N-1))

    # Calcular o erro absoluto
    errors = np.abs(U_exata - U_numerica) # Erro em módulo
    df = pd.DataFrame(errors, 
                      columns=[f"Erro y={i/(N+1):.2f}" for i in range(N+1)],
                      index=[f"x={i/(N+1):.2f}" for i in range(N+1)])
    return df
```

Logo, com a coletânea de funções necessárias basta resolver o sistema, calcular o erro relativo à $u_{exata}$ e assim plotar simulações em cada $N$.

```py
def solve_system(N, f, u):
    g = lambda x,y: u(x,y)

    A, b = poisson_system(N, f, g)        #(i)
    numeric = linalg.spsolve(A,b)         #(ii)
    plot_solutions(N, u, numeric)         #(iii)
    print(error_function(N, u, numeric))  #(iv)

print("Simulações")
for N in [50, 100, 200]:
    print(f"N = {N}")
    solve_system(N, f, u)

```



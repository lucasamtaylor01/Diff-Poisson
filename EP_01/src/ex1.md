## Exercício 1

Iniciamos pela definição das funções que vão compor essencialmente o problema.

```python
# Função u (item a)
u = lambda x, y: x**4 - 6*x**2*y**2 + y**4
f_u = lambda x, y: -12*(x**2 + y**2)

# Função v (item b)
v = lambda x, y: np.exp(x) * np.sin(y)
f_v = lambda x, y: 0
```

Cada $f$ foi encontrada como $-\Delta u$, no entanto laplacianos calculados manualmente em cada caso.


Em seguida podemos estruturar a função que cria $A$ e $b$ para resolução do sistema $AU = b$. Note que essa função será necessária nos dois exercícios solicitados.

```py
def poisson_system(N: int, f: float, g: float):
    h = 1/N
    n = (N-1)**2 # número de variáveis presentes no sistema
    diagonals = [-1, -1, 4, -1, -1] # valores que serão atribuidos as diagonais de A
    offsets = [-N+1, -1, 0, 1, N-1] # confere o deslocamento das diagonais
    
    # matriz A iniciada
    A: csc_array = diags(diagonals=diagonals, offsets=offsets, shape=(n,n)).tocsc()
    
    # vetor b (termos da equação e cond. de contorno)
    b = np.zeros(n)

    # Preenchimento de b com f (pontos internos)
    for k in range(1, N):
        for j in range(1, N):
            i = (k - 1) * (N-1) + (j-1) # indice lexicográfico
            x, y = k * h, j * h
            b[i] = h ** 2 * f(x, y)
    
    # Bordas (esq -> dir) & (inf -> sup): condições de contorno
            if k == 1:
                b[i] -= g(0, y)  # borda esquerda
            if k == N - 1:
                b[i] -= g(1, y)  # borda direita
            if j == 1:
                b[i] -= g(x, 0)  # borda inferior
            if j == N - 1:
                b[i] -= g(x, 1)  # borda superior
    
    return A, b
```

Intrinsecamente, esta função será chave para resolução

Ao final só precisaremos estabelecer $g$ como 

```py
g = lambda x,y: exact(x,y) # atribui  u_exata no caso solicitado
```

E por fim ao encontrar $A$ e $b$, basta solucionar o sistema que nos devolve a solução numérica e assim realizar a visualização gráfica.

```py
A, b = poisson_system(N, f, g)
numeric = linalg.spsolve(A,b)
plot_solution(N, exact, numeric, title)   
```



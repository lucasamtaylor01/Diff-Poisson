'''
Exercício 1 - resolução 
a) u(x, y) = x^4 − 6x^2y^2 + y^4
b) u(x, y) = exp(x) * sin(y)
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags, linalg

global option # variável de escolha do item

# Definindo as funções

u = lambda x,y: x**4 - 6*x**2*y**2 + y**4 # item (a)   
f_u = lambda x,y: -12*(x**2 + y**2)

v = lambda x,y: np.exp(x) * np.sin(y) # item (b)
f_v = lambda x,y: 0

# Função que desenvolve o sistema de Poisson
def poisson_system(N: int, f: float, g: float):
    h = 1/N
    n = (N-1)**2 
    diagonals = [-1, -1, 4, -1, -1]
    offsets = [-N+1, -1, 0, 1, N-1] #confere o deslocamento das diagonais
    
    # matriz A 
    A: csc_array = diags(diagonals=diagonals, offsets=offsets, shape=(n,n)).tocsc()
    
    # vetor b (termos da equação e cond. de contorno)
    b = np.zeros(n)

    # Preenchimento de b com f (pontos internos)
    for k in range(1, N):
        for j in range(1, N):
            i = (k - 1) * (N-1) + (j-1) # ordem lexicográfica
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

# Função que plota as soluções no espaço e no mapa de curvas de nível
def plot_solution(N: int, exact_sol: float, numeric_sol: float, title: str):
    x = np.linspace(0, 1, N+1)
    y = np.linspace(0, 1, N+1)
    X, Y = np.meshgrid(x, y)

    # Solução exata
    exact = exact_sol(X, Y)

    # Inserir solução numérica nos pontos internos
    numeric = np.zeros((N+1, N+1))
    numeric[1:N, 1:N] = numeric_sol.reshape((N-1, N-1))

    # Gráficos
    fig = plt.figure(figsize=(12, 6))

    # Gráfico 3D da solução exata
    ax1 = fig.add_subplot(121, projection='3d')
    ax1.plot_surface(X, Y, exact, cmap='plasma')
    ax1.set_title(f"Solução exata ($u_{{exata}}$) da {title} - N={N}")
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('u')

    # Gráfico de contorno (curvas de nível)
    ax2 = fig.add_subplot(122)
    contour = ax2.contourf(X, Y, exact, cmap='plasma')
    fig.colorbar(contour, ax=ax2)
    ax2.set_title(f"Curvas de nível de $u_{{exata}}$")
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')

    plt.show()

# Função que resolve o exercício
def prompt():
    print(f"{'='* 10} Escolha {'='* 10}\n")
    print("(1) u(x, y) = x^4 - 6x^2y^2 + y^4\n(2) u(x, y) = exp(x) * sin(y)")
    option = int(input("_:"))

    if option == 1:
        exact = u
        f = f_u
        title = 'u(x, y) = x^4 - 6x^2y^2 + y^4'
    elif option == 2:
        exact = v
        f = f_v
        title = 'u(x, y) = exp(x) * sin(y)'
    else:
        print("Escolha inválida.")
        return
    
    g = lambda x,y: exact(x,y) # atribui cada u_exata

    print(f"{'='* 10} Escolha N {'='* 10}\n")
    n = int(input("(1) 20\n(2) 50\n(3) 100\n_:"))

    if n == 1: N = 20
    elif n == 2: N = 50
    else: N = 100

    A, b = poisson_system(N, f, g)
    numeric = linalg.spsolve(A,b)
    plot_solution(N, exact, numeric, title)   

prompt() # Execução principal
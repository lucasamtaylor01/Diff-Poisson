import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.sparse import diags, linalg

# Função exata u_exata e função f para a equação de Poisson
def u_exata(x, y):
    return np.cos(x) * np.sin(y)

def f(x, y):
    return -2 * np.cos(x) * np.sin(y)

# Item a: Verificar se u_exata satisfaz a equação com a função de força f
def verificar_solucao():
    x_vals = np.linspace(0, 1, 5)
    y_vals = np.linspace(0, 1, 5)
    for x in x_vals:
        for y in y_vals:
            lhs = f(x, y)  # Lado esquerdo da equação (função de força)
            rhs = -2 * np.cos(x) * np.sin(y)  # Lado direito usando u_exata
            if not np.isclose(lhs, rhs):
                print(f"Erro: para (x={x}, y={y}), LHS = {lhs}, RHS = {rhs}")
                return False
    print("A solução u_exata(x, y) satisfaz a equação com a função de força f(x, y).")
    return True

# Função para montar a matriz A e o vetor b usando diferenças finitas centradas
def montar_sistema_poisson(N, f, g):
    h = 1 / N
    n = (N - 1) ** 2  # Número de incógnitas
    A = diags([-1, -1, 4, -1, -1], [-N + 1, -1, 0, 1, N - 1], shape=(n, n)).tocsc()  # Matriz esparsa
    b = np.zeros(n)

    # Preencher o vetor b com f e condições de contorno
    for i in range(1, N):
        for j in range(1, N):
            k = (i - 1) * (N - 1) + (j - 1)  # Índice lexicográfico
            x, y = i * h, j * h
            b[k] = h**2 * f(x, y)
            if i == 1:
                b[k] -= g(0, y)  # Condição na borda esquerda
            if i == N - 1:
                b[k] -= g(1, y)  # Condição na borda direita
            if j == 1:
                b[k] -= g(x, 0)  # Condição na borda inferior
            if j == N - 1:
                b[k] -= g(x, 1)  # Condição na borda superior

    return A, b

# Função para calcular o erro absoluto entre a solução exata e a numérica
def calcular_erros(N, u_exata, u_numerica):
    h = 1 / N
    x = np.linspace(0, 1, N+1)
    y = np.linspace(0, 1, N+1)
    X, Y = np.meshgrid(x, y)

    # Solução exata nos pontos da grade
    U_exata = u_exata(X, Y)

    # Inserir solução numérica nos pontos internos
    U_numerica = np.zeros((N+1, N+1))
    U_numerica[1:N, 1:N] = u_numerica.reshape((N-1, N-1))

    # Calcular o erro absoluto
    erros = np.abs(U_exata - U_numerica)
    return erros

# Função para imprimir os erros usando Pandas (Item c)
def imprimir_erros(N, u_exata, u_numerica):
    erros = calcular_erros(N, u_exata, u_numerica)
    
    # Criar um DataFrame do Pandas com os erros
    df = pd.DataFrame(erros, columns=[f"Erro y={i/(N+1):.2f}" for i in range(N+1)],
                      index=[f"x={i/(N+1):.2f}" for i in range(N+1)])
    print(df)

# Função para plotar a solução exata e numérica (Item b)
def plotar_solucoes(N, u_exata, u_numerica):
    h = 1 / N
    x = np.linspace(0, 1, N+1)
    y = np.linspace(0, 1, N+1)
    X, Y = np.meshgrid(x, y)

    # Solução exata
    U_exata = u_exata(X, Y)

    # Inserir solução numérica nos pontos internos
    U_numerica = np.zeros((N+1, N+1))
    U_numerica[1:N, 1:N] = u_numerica.reshape((N-1, N-1))

    # Plotar solução exata
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.contourf(X, Y, U_exata, cmap='plasma')
    plt.colorbar()
    plt.title('Solução Exata')

    # Plotar solução numérica
    plt.subplot(1, 2, 2)
    plt.contourf(X, Y, U_numerica, cmap='plasma')
    plt.colorbar()
    plt.title('Solução Numérica')

    plt.show()

# Função principal para resolver o problema (Itens b e c)
def resolver_poisson(N, f, u_exata):
    # Definir as condições de contorno (g) como a própria solução exata
    def g(x, y):
        return u_exata(x, y)

    # Montar o sistema linear
    A, b = montar_sistema_poisson(N, f, g)

    # Resolver o sistema linear
    u_numerica = linalg.spsolve(A, b)

    # Plotar as soluções (Item b)
    plotar_solucoes(N, u_exata, u_numerica)

    # Imprimir os erros (Item c)
    imprimir_erros(N, u_exata, u_numerica)

# Chamar funções para resolver o exercício 2
def main():
    print("Resolvendo o exercício 2...")

    # Item a: Verificar se a solução satisfaz a equação
    print("Item a: Verificando a solução...")
    verificar_solucao()

    # Item b: Resolver e plotar para N = 50, 100, 200
    for N in [50, 100, 200]:
        print(f"\nItem b e c: Resultados para N = {N}")
        resolver_poisson(N, f, u_exata)

if __name__ == "__main__":
    main()

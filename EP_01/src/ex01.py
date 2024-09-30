import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags, linalg

# Definir as funções u_exata e f para a equação (a)
def u_exata_a(x, y):
    return x**4 - 6*x**2*y**2 + y**4

def f_a(x, y):
    return -12*(x**2 + y**2)

# Definir as funções u_exata e f para a equação (b)
def u_exata_b(x, y):
    return np.exp(x) * np.sin(y)

def f_b(x, y):
    return -np.exp(x) * np.sin(y)

# Função para criar a matriz A e o vetor b usando diferenças finitas centradas
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

# Função para plotar a solução
def plot_solution(N, u_exata, u_numerica, titulo):
    h = 1 / N
    x = np.linspace(0, 1, N+1)
    y = np.linspace(0, 1, N+1)
    X, Y = np.meshgrid(x, y)

    # Solução exata
    U_exata = u_exata(X, Y)

    # Inserir solução numérica nos pontos internos
    U_numerica = np.zeros((N+1, N+1))
    U_numerica[1:N, 1:N] = u_numerica.reshape((N-1, N-1))

    # Gráficos
    fig = plt.figure(figsize=(12, 6))

    # Gráfico 3D da solução exata
    ax1 = fig.add_subplot(121, projection='3d')
    ax1.plot_surface(X, Y, U_exata, cmap='plasma')
    ax1.set_title(f"Solução exata ($u_{{exata}}$) da {titulo}")
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('u')

    # Gráfico de contorno (curvas de nível)
    ax2 = fig.add_subplot(122)
    contour = ax2.contourf(X, Y, U_exata, cmap='plasma')
    fig.colorbar(contour, ax=ax2)
    ax2.set_title(f"Curvas de nível de $u_{{exata}}$")
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')

    plt.show()

# Perguntar ao usuário qual equação e valor de N deseja utilizar
def main():
    print("Escolha uma equação para resolver:")
    print("1 - u(x, y) = x^4 - 6x^2y^2 + y^4")
    print("2 - u(x, y) = exp(x) * sin(y)")

    escolha_eq = input("Digite o número da equação (1 ou 2): ")
    if escolha_eq == '1':
        u_exata = u_exata_a
        f = f_a
        titulo = "Equação de Poisson (a)"
    elif escolha_eq == '2':
        u_exata = u_exata_b
        f = f_b
        titulo = "Equação de Poisson (b)"
    else:
        print("Escolha inválida.")
        return

    print("\nEscolha um valor de N:")
    print("1 - N = 20")
    print("2 - N = 50")
    print("3 - N = 100")

    escolha_N = input("Digite o número correspondente ao valor de N: ")
    if escolha_N == '1':
        N = 20
    elif escolha_N == '2':
        N = 50
    elif escolha_N == '3':
        N = 100
    else:
        print("Escolha inválida.")
        return

    # Definir as condições de contorno (g) como a própria solução exata
    def g(x, y):
        return u_exata(x, y)

    # Montar o sistema linear
    A, b = montar_sistema_poisson(N, f, g)

    # Resolver o sistema linear usando scipy.sparse.linalg
    u_numerica = linalg.spsolve(A, b)

    # Chamar a função para plotar a solução
    plot_solution(N, u_exata, u_numerica, titulo)

if __name__ == "__main__":
    main()

import numpy as np
import matplotlib.pyplot as plt

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

# Função para plotar a solução
def plot_solution(N, u_exata, f, titulo):
    h = 1 / N
    x = np.linspace(0, 1, N+1)
    y = np.linspace(0, 1, N+1)
    X, Y = np.meshgrid(x, y)

    # Solução exata
    U_exata = u_exata(X, Y)

    # Gráficos
    fig = plt.figure(figsize=(12, 6))

    # Gráfico 3D
    ax1 = fig.add_subplot(121, projection='3d')
    ax1.plot_surface(X, Y, U_exata, cmap='plasma')
    ax1.set_title(f"Solução exata ($u_{{exata}}$) da {titulo}")
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('u')

    # Gráfico de contorno
    ax2 = fig.add_subplot(122)
    contour = ax2.contourf(X, Y, U_exata, cmap='plasma')
    fig.colorbar(contour)
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

    # Chamar a função para plotar a solução
    plot_solution(N, u_exata, f, titulo)

if __name__ == "__main__":
    main()

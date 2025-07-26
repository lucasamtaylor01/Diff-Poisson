# 🧮 Finite Difference Method for the Poisson Equation

This repository presents a numerical study of the **Dirichlet problem** for the **Poisson equation** on the unit square $(0, 1) \times (0, 1)$, using the **finite difference method**. The domain is discretized with step size $h = \frac{1}{N} $, and the resulting system is solved efficiently via sparse matrix techniques and lexicographic ordering.

## 📘 Problem Statement

We aim to solve the Poisson equation:


$$- \Delta u(x, y) = f(x, y), \quad (x, y) \in \Omega = (0, 1) \times (0, 1)$$

subject to Dirichlet boundary conditions:

$$u(x, y) = g(x, y), \quad (x, y) \in \partial\Omega$$

## ⚙️ Methodology

- **Discretization**: The Laplacian is approximated using the second-order centered finite difference method.
- **System Assembly**: The discrete equations form a linear system $AU = b$, solved using sparse direct solvers.
- **Grid Refinement**: Simulations are run for increasing values of $N$ to verify convergence.
- **Validation**: Numerical solutions are compared against exact solutions, and error tables are generated.

## 🧪 Features

- Supports custom forcing terms $f(x, y)$ and exact solutions for benchmarking
- Handles Dirichlet boundary conditions directly
- Produces 3D surface plots of the numerical and exact solutions
- Exports error tables for each simulation as `.csv` files

## 🛠 Dependencies

This project uses the following Python libraries:

- [`numpy`](https://numpy.org/)
- [`scipy`](https://scipy.org/)
- [`matplotlib`](https://matplotlib.org/)
- [`pandas`](https://pandas.pydata.org/)
- [`prettytable`](https://pypi.org/project/prettytable/)
- [`tabulate`](https://pypi.org/project/tabulate/)

## 📁 Repository Structure
```
Diff-Poisson/
├── 01_src/ # Jupyter notebooks with source code
├── 02_assets/ # Simulation plots (PNG)
├── 03_data/ # Error tables (CSV)
├── 04_report/ # Final report and LaTeX files
├── README.md
├── LICENSE
```

## 📊 Example Simulations

Two exact solutions were used for validation:

- $u(x, y) = x^4 - 6x^2 y^2 + y^4$
- $u(x, y) = e^x \sin(y)$

Simulations were performed with $N = 20, 50, 100, 200$. Plots and error tables are available in the respective folders.

## 📄 Report

The full documentation of this project can be found in [`04_report/Finite_Difference_Solution_of_the_Poisson_Equation.pdf`](./04_report/Finite_Difference_Solution_of_the_Poisson_Equation.pdf).

## 👥 Authors

- **[Julio Cezar de Moura Lima](https://github.com/Juliocezar7253)**
- **[Lucas Amaral Taylor](https://github.com/lucasamtaylor01)**

# Study of the Dirichlet Problem for the Poisson Equation with Finite Discretization

This repository focuses on the Dirichlet problem for the Poisson equation, which is discretized over the unit square using the finite difference method with spacing $h = \frac{1}{N}$. The equations describing $U_{mn}$, along with the boundary conditions, are organized into a linear system. This system is then solved using lexicographic ordering to facilitate the numerical solution process.

## Problem Description 📝

The Poisson equation we aim to solve is given by:

$-\Delta u(x, y) = f(x, y), \quad (x, y) \in \Omega$

where $\Omega = (0, 1) \times (0, 1)$, and Dirichlet boundary conditions are imposed on the boundary $\partial\Omega$.

## Tools Used 🔧

To implement and solve the problem, we use the following Python libraries:

- **NumPy**: For array and matrix manipulation.
- **SciPy**: For iterative methods and sparse matrix storage.
- **Matplotlib**: For graphical visualization of the solutions.
- **Pandas, PrettyTable, and Tabulate**: For organizing and displaying errors in tables.

## Methodology 💻

1. **Discretization**: We apply the centered finite difference method.
2. **Solving the Linear System**: An iterative method is used to solve the linear system resulting from the discretization.
3. **Simulations**: Simulations are run for different values of $N$ (mesh size).

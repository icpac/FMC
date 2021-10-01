from sympy import symbols, Eq, solve

x = symbols('x')

solc = solve(x**3 - 2*x**2+1)
print(solc)


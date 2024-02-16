from sympy import integrate, symbols, tan

# Define the symbols
x, y, z = symbols('x y z')

# Expressions to integrate
expr1 = 3*x**2 + 4*y**3
expr2 = x**2 * y
expr3 = 1  # 'a' is a constant
expr4 = 6*x*y*z

# Calculating the double integrals
integral1 = integrate(integrate(expr1, (y, 0, 1)), (x, 1, 2))
integral2 = integrate(integrate(expr2, (x, 0, 2)), (y, 1, 3))
integral3 = integrate(integrate(expr3, (y, 3, 6)), (x, 0, 2), (z, -2, 2))
integral4 = integrate(integrate(expr4, (y, 0, 1)), (x, -1, 2), (z, -1, 1))

print(integral1, integral2, integral3, integral4)



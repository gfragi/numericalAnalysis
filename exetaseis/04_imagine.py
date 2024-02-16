from sympy import symbols, I, simplify

# Define the complex number in standard form a + I*b
z = ((3 + 3*I)/(I - 1))**2 
w = ((2 - 3*I)/(2 + 3*I)) - ((1 - I)/(2 - I))
t = ((1 + 2*I)/(2 - I)) + (2/I)
h = (1 + 2*I) ** 3 - (2 - I)**3

# Simplify the complex number to standard form
z_simplified = simplify(z)
w_simplified = simplify(w)
t_simplified = simplify(t)
h_simplified = simplify(h)



print(z_simplified)
print(w_simplified)
print(t_simplified)
print(h_simplified)

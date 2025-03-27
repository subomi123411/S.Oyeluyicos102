import sympy as sp

def solve_quadratic():
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    x = sp.symbols('x')
    roots = sp.solve(a * x**2 + b * x + c, x)
    print("Roots:", roots)

def solve_cubic():
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    d = float(input("Enter coefficient d: "))
    x = sp.symbols('x')
    roots = sp.solve(a * x**3 + b * x**2 + c * x + d, x)
    print("Roots:", roots)

def solve_quartic():
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    d = float(input("Enter coefficient d: "))
    e = float(input("Enter coefficient e: "))
    x = sp.symbols('x')
    roots = sp.solve(a * x**4 + b * x**3 + c * x**2 + d * x + e, x)
    print("Roots:", roots)

print("Choose the equation type:")
print("1. Quadratic (ax^2 + bx + c = 0)")
print("2. Cubic (ax^3 + bx^2 + cx + d = 0)")
print("3. Quartic (ax^4 + bx^3 + cx^2 + dx + e = 0)")

choice = input("Enter your choice (1/2/3): ")

if choice == '1':
    solve_quadratic()
elif choice == '2':
    solve_cubic()
elif choice == '3':
    solve_quartic()
else:
    print("Invalid choice!")

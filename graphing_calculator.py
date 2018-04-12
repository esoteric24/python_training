from sympy import Symbol, sympify, solve
from sympy.plotting import plot

y = Symbol('y')
x = Symbol('x')

colors = ['b', 'r', 'g', 'c', 'm', 'y']

def format_equation(expr):
    y = Symbol('y')
    solutions = solve(expr, y)
    if solutions == []:
        return expr
    else:
        equation = solutions[0]
        return equation

equations = []

print(' ')
print('This program graphs up to six equations using SymPy.')
print(' ')

while True:
    equation = input('Enter an equation in terms of x and y that you wish to graph: ')
    print(' ')
    answer = input('Do you wish to input another equation to graph? y for yes, n for no: ')
    print(' ')
    try:
        equation = sympify(equation)
    except SympifyError:
        print('Invalid input')
    else:
        equation = format_equation(equation)
        equations.append(equation)
        if answer == 'n':
            break

numLines = len(equations)
p = plot(*equations, legend=True, show=False)
for num in range(numLines):
    p[num].line_color = colors[num]
p.show()

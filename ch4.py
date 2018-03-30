from sympy import Symbol, pprint, init_printing

def print_series(n, x_value):
    init_printing(order='rev-lex')
    x = Symbol('x')
    series = x
    for i in range(2, n+1):
        series = series + (x**i)/i

    pprint(series)

    series_value = series.subs({x:x_value})
    print('Value of the series when x equals {0}: {1}'.format(x_value, series_value))

# n = input('Enter the number of terms you want in the series: ')
# x_value = input('Enter the value of x at which you want to evaluate the series: ')
# print_series(int(n), float(x_value))

from sympy import expand, sympify
from sympy.core.sympify import SympifyError

def product(expr1, expr2):
    prod = expand(expr1*expr2)
    print(prod)

# expr1 = input('Enter the first expression: ')
# expr2 = input('Enter the second expression: ')

try:
    expr1 = sympify(expr1)
    expr2 = sympify(expr2)
except SympifyError:
    print('Invalid input')
else:
    product(expr1, expr2)

from sympy import Symbol, sympify, solve
from sympy.plotting import plot

def plot_expression(expr):
    y = Symbol('y')
    solutions = solve(expr, y)
    expr_y = solutions[0]
    plot(expr_y)

# expr = input('Enter your expression in terms of x and y: ')

try:
    expr = sympify(expr)
except SympifyError:
    print('Invalid input')
else:
    plot_expression(expr)

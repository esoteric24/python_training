from sympy import Poly, Symbol, sin, cos, tan
from sympy import solve_poly_inequality, solve_rational_inequalities, solve_univariate_inequality

def poly_ineq(ineq):
    x = Symbol('x')
    lhs = ineq.lhs
    p = Poly(lhs, x)
    rel = ineq.rel_op
    solution = solve_poly_inequality(p, rel)
    return solution

def rational_ineq(ineq):
    x = Symbol('x')
    lhs = ineq.lhs
    numer, denom = lhs.as_numer_denom()
    p1 = Poly(numer)
    p2 = Poly(denom)
    rel = ineq.rel_op
    solution = solve_rational_inequalities([[((p1, p2), rel)]])
    return solution

def otherwise_ineq(ineq):    

def identify_ineq(ineq):
    x = Symbol('x')
    expr = ineq.lhs
    polyIden = expr.is_polynomial()
    rationIden = expr.is_rational_function()
    if polyIden == True:
        solution = poly_ineq(ineq)
        return solution
    elif rationIden == True:
        solution = rational_ineq(ineq)
        return solution
    else:
        return 'univariate'

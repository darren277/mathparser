""""""
import argparse
import requests
from bs4 import BeautifulSoup


def fetch_from_wikipedia(page, section_id):
    soup = BeautifulSoup(requests.get(f'https://en.wikipedia.org/wiki/{page}').text)
    section = soup.find('span', {'id': section_id}).parent.nextSibling.nextSibling
    return section


def main(src: str, latex: bool, mathml: bool):
    #from src.inprogress import parse_latex
    #from src.inprogress import parse_mathml
    #parsed = parse_latex(fetch_from_wikipedia('Discrete_cosine_transform', 'DCT-I').find('annotation', {'encoding': 'application/x-tex'}).text)
    #parsed = parse_mathml(fetch_from_wikipedia('Discrete_cosine_transform', 'DCT-I').find('annotation', {'encoding': 'application/x-tex'}).text)
    print(src)



f_x = lambda x: x**2

f_x = lambda x: 6*x**3 + 14*x**2 - 25*x + 4

# l: ast.Lambda
# args, body = l.args, l.body

# ast.parse

import ast

OPERATORS = {
    #ast.Mult: '*',
    ast.Mult: '',
    ast.Add: ' + ',
    ast.Sub: ' - ',
    ast.Div: '/',
    ast.Pow: '^'
}

def process_bin_op(bin_op: ast.BinOp) -> str:
    left = bin_op.left
    right = bin_op.right
    op = bin_op.op

    print('left op right', left, op, right)

    lp, rp = '', ''
    # lp, rp = '(', ')'

    if type(left) == ast.BinOp:
        lhs = process_bin_op(left)
    elif type(left) == ast.Constant:
        lhs = left.value
    elif type(left) == ast.Name:
        lhs = left.id
    else:
        raise ValueError(f'Unexpected type: {type(left)}')

    if type(right) == ast.BinOp:
        rhs = process_bin_op(right)
    elif type(right) == ast.Constant:
        rhs = right.value
    elif type(right) == ast.Name:
        rhs = right.id
    else:
        raise ValueError(f'Unexpected type: {type(right)}')

    return f"{lp}{lhs}{OPERATORS.get(type(op), '?')}{rhs}{rp}"


# The difference between a function and an equation is that a function is a mapping from a domain to a codomain,
# whereas an equation is a statement that two expressions are equal.

# Can all equations be represented as functions?
# Can all functions be represented as equations?

# Answers:
# 1. Yes, all equations can be represented as functions (???).
# 2. No, not all functions can be represented as equations (???).



class Equation:
    _type: str

    def __init__(self, eq: str):
        self.eq = eq
        self.terms = []

    @property
    def number_of_terms(self):
        return len(self.terms)

    def parse(self):
        # TODO: Work in progress.
        ...

    def latex(self):
        # TODO: For a later iteration.
        pass

    def plot(self):
        # TODO: For a later iteration.
        pass


class LinearEquation(Equation):
    _type = 'linear'

    def convert_to_standard_form(self):
        # ax + b = 0
        # ax + by + c = 0
        ...

    def convert_to_slope_intercept_form(self):
        # y = mx + b
        ...

    def convert_to_point_slope_form(self):
        # y - y1 = m(x - x1)
        ...



class QuadraticEquation(Equation):
    _type = 'quadratic'


class CubicEquation(Equation):
    _type = 'cubic'


class RationalEquation(Equation):
    _type = 'rational'


#class PolynomialEquation(Equation): _type = 'polynomial'
# polynomial vs quadratic: degree > 2 (???)



class SystemOfEquations:
    def __init__(self, *eqs: Equation):
        self.eqs = eqs

    def solve_by_substitution(self):
        ...

    def solve_by_elimination(self):
        ...

    def solve_by_graphing(self):
        ...



def parse_function(func: callable):
    import ast
    import inspect

    # parse the function
    code = inspect.getsource(func)

    parsed = ast.parse(code)
    print('parsed:', parsed)

    body = parsed.body[0]

    if type(body) != ast.Assign:
        raise ValueError('Function must be a single assignment')

    targets = body.targets
    value = body.value

    print('targets', targets)
    print('value', value)

    if type(value) != ast.Lambda:
        raise ValueError('Function must be a lambda')

    args = value.args
    body = value.body

    print('args', args)
    # ast.arguments
    print('args.args', args.args)
    print('body', body)

    s = ""

    if type(body) == ast.BinOp:
        s += process_bin_op(body)
    elif type(body) == ast.Call:
        # if special case of `log()`:
        if type(body.func) == ast.Name and body.func.id == 'log':
            s += 'log_'
            x = body.args[0]
            if type(x) == ast.Constant:
                s += str(x.value)
            elif type(x) == ast.BinOp:
                s += process_bin_op(x)
            else:
                raise ValueError('Unexpected type')
            base = body.args[1]
            if type(base) == ast.Constant:
                s += f"({base.value})"
            else:
                raise ValueError('Unexpected type')

            #breakpoint()
    else:
        raise ValueError('Unexpected type')

    print('s', s)

    #breakpoint()


parse_function(f_x)

eq = '6x^3 + 14x^2 - 25x + 4'

number_of_terms = 4


f_x = lambda x: (x + 2) / (x**2 + x - 1)

parse_function(f_x)



# Logarithm example...
eq = 'log_2(8)'

from math import log

f_x = lambda x: log(8, 2)

parse_function(f_x)

# log_b(A) = C <==> b^C = A

# Product Rule: log_b(A) + log_b(C) = log_b(A * C)
# Quotient Rule: log_b(A) - log_b(C) = log_b(A / C)
# Power Rule: log_b(A^C) = C * log_b(A)

def apply_product_rule(log_func: callable):
    # 1. Verify that it satisfies the correct pattern...
    ...

    # 2. Apply the rule...
    ...


# example linear equation for using slope formula...
eq = 'y = 2x + 3'

f_x = lambda x: 2*x + 3

parse_function(f_x)

def slope_function(x1, y1, x2, y2):
    m = (y2 - y1) / (x2 - x1)
    return m

def slope_intercept(m, x, b):
    return m*x + b



# Factoring Polynomials

# Smple monomial factoring:
eq = lambda x: 2*x**2 + 18*x

# Quadratic factoring:
eq = lambda x: x**2 + 5*x + 6



def quadratic_formula(a, b, c):
    import math
    d = math.sqrt(b**2 - 4*a*c)
    x1 = (-b + d) / (2*a)
    x2 = (-b - d) / (2*a)
    return x1, x2



# Simplifying Radicals and Exponents:

eq = lambda x: math.sqrt(48)
# = 4 * sqrt(3)



# Fractional Exponents:

# Negative Exponents:
# a^-m = 1 / a^m

# Fractional Exponents:
# a^(m/n) = n√a^m




# Solving Systems of Equations






quit(34)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('src')
    parser.add_argument('--latex', default=True)
    parser.add_argument('--mathml', default=False)

    args = parser.parse_args()
    print(args)
    main(args.src, args.latex, args.mathml)




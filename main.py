""""""
import argparse
import requests
from bs4 import BeautifulSoup
import sympy as sp

import math

from src.lib.eq import System, Equation

# Log 10 (default base)...
# log(x) = log_10(x)

# Log base 2...
# log_2(x)

# Natural log...
# ln(x) = log_e(x)

# Log base b...
# log_b(x)

# Change of base formula:
# log_b(x) = log_c(x) / log_c(b)


## EXAMPLES

# log_2(8) = 3
result = math.log(8, 2)
print(result)
assert result == 3



# log_b(xy) = log_b(x) + log_b(y)

# log_b(x/y) = log_b(x) - log_b(y)

# log_b(x^y) = y * log_b(x)




def test():
    x, y = sp.symbols('x y')
    eq1 = Equation.from_string("2*x + 3*y = 7")
    eq2 = Equation.from_string("x - y = 1")
    system = System((eq1, eq2))
    print(system.solve(x, y))  # {x: 2, y: 1}


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



class Function:
    _type: str
    _degree: int


def parse_equation(lhs: callable, rhs: callable) -> Equation:
    """
    Takes in two mathematical expressions defined as Lambda functions and parses it into an Equation object.
    :param func:
    :return:
    """
    import ast
    import inspect

    # parse the function
    lhs_code = inspect.getsource(lhs)

    parsed = ast.parse(lhs_code)
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


f_x = lambda x: x**2

f_x = lambda x: 6*x**3 + 14*x**2 - 25*x + 4

#parse_function(f_x)

eq = '6x^3 + 14x^2 - 25x + 4'

number_of_terms = 4


f_x = lambda x: (x + 2) / (x**2 + x - 1)

#parse_function(f_x)



# Logarithm example...
eq = 'log_2(8)'

from math import log

f_x = lambda x: log(8, 2)

#parse_function(f_x)

# log_b(A) = C <==> b^C = A

# Product Rule: log_b(A) + log_b(C) = log_b(A * C)
# Quotient Rule: log_b(A) - log_b(C) = log_b(A / C)
# Power Rule: log_b(A^C) = C * log_b(A)


eq = parse_equation(
    lambda: log(5, 9) - log(5, 11),
    lambda x: log(5, x)
)


eq_str = "log(5, 9) - log(5, 11) = log(5, x)"

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




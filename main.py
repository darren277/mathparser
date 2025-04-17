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
    # 1. Build an equation from a string
    eq = Equation.from_string("x**2 + 1 = 5")
    print(eq.type(), eq.degree)  # quadratic 2
    print(eq.terms)  # [x**2, -4]

    # 2. Solve
    print(eq.solve())  # [-2, 2]

    # 3. Pretty print
    print(eq.latex())  # x^{2} + 1 = 5

    # 4. Plot
    eq.plot()
    # pops up matplotlib window

    x, y = sp.symbols('x y')
    eq1 = Equation.from_string("2*x + 3*y = 7")
    eq2 = Equation.from_string("x - y = 1")
    system = System((eq1, eq2))
    print(system.solve(x, y))  # {x: 2, y: 1}

# Logarithm example...
eq = 'log_2(8)'

from math import log

f_x = lambda x: log(8, 2)

#parse_function(f_x)

# log_b(A) = C <==> b^C = A

# Product Rule: log_b(A) + log_b(C) = log_b(A * C)
# Quotient Rule: log_b(A) - log_b(C) = log_b(A / C)
# Power Rule: log_b(A^C) = C * log_b(A)


#eq = parse_equation(
#    lambda: log(5, 9) - log(5, 11),
#    lambda x: log(5, x)
#)


def test_logarithms():
    LOCAL_DICT = {
        'log': sp.log,  # base‑aware
        'ln': sp.log,  # alias
    }

    expr = sp.sympify("log(x, 2) + ln(y)", locals=LOCAL_DICT)
    #print(expr)


    eq_str = "log(9, 5) - log(11, 5) = log(x, 5)"

    # 1. Build an equation from a string
    eq = Equation.from_string(eq_str)
    print(eq.type(), eq.degree)  # quadratic 2

    # 2. Solve
    print(eq.solve())

    # 3. Pretty print
    #print(eq.latex())

    # Apply product rule...
    eq = eq.apply_quotient_rule()
    print(eq.type(), eq.degree)
    print(eq.terms)


#test()

test_logarithms()



quit(23)


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



class Function:
    _type: str
    _degree: int



f_x = lambda x: x**2

f_x = lambda x: 6*x**3 + 14*x**2 - 25*x + 4

#parse_function(f_x)

eq = '6x^3 + 14x^2 - 25x + 4'

number_of_terms = 4


f_x = lambda x: (x + 2) / (x**2 + x - 1)

#parse_function(f_x)




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




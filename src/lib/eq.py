""""""
from dataclasses import dataclass
from typing import Union

import sympy as sp

# The difference between a function and an equation is that a function is a mapping from a domain to a codomain,
# whereas an equation is a statement that two expressions are equal.

# Can all equations be represented as functions?
# Can all functions be represented as equations?

# Answers:
# 1. Yes, all equations can be represented as functions (???).
# 2. No, not all functions can be represented as equations (???).



class EquationOld:
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


class LinearMixin:
    def to_standard(self):
        # ax + by + c = 0
        a, b, c = sp.Poly(self.symbolic).coeffs()
        return f"{a}x + {b}y + {c} = 0"

    def to_slope_intercept(self):
        # y = mx + b  (solve for y)
        y = sp.symbols('y')
        mform = sp.solve(self.expr, y)[0]
        return sp.simplify(mform)

    def to_point_slope(self, x1, y1):
        m = sp.diff(self.lhs, sp.symbols('x'))  # or compute slope from two points
        return f"y - {y1} = {m}(x - {x1})"


@dataclass(frozen=True)
class Equation:
    lhs: Union[sp.Expr, int, float]
    rhs: Union[sp.Expr, int, float]

    @classmethod
    def from_string(cls, s: str, symbols: str = "x y"):
        """Ex: 'x**2 + 1 = 5'."""
        syms = sp.symbols(symbols)
        left, right = [sp.sympify(part, locals=dict(zip(symbols.split(), syms))) for part in s.split('=')]
        return cls(left, right)

    @classmethod
    def from_lambda(cls, lam):
        """Ex: lambda x: x**2 + 1 - 5."""
        # relies on inspect+ast or simply __code__.co_consts if simple
        import inspect, textwrap
        src = textwrap.dedent(inspect.getsource(lam))
        expr = sp.sympify(src.split(':', 1)[1])
        return cls(expr, 0)

    # ---------- quick properties ----------
    @property
    def expr(self) -> sp.Eq:
        return sp.Eq(self.lhs, self.rhs)

    @property
    def symbolic(self) -> sp.Expr:
        """Bring everything to one side (lhs‑rhs)."""
        return sp.simplify(self.lhs - self.rhs)

    @property
    def degree(self):
        return sp.degree(self.symbolic)

    @property
    def terms(self):
        return sp.expand(self.symbolic).as_ordered_terms()

    # ---------- high‑level operations ----------
    def solve(self, *symbols):
        return sp.solve(self.expr, *symbols)

    def latex(self):
        return sp.latex(self.expr)

    def plot(self, var='x', rng=(-10, 10)):
        sp.plot_implicit(self.expr, (sp.symbols(var), *rng), show=True)

    # ---------- classification ----------
    def type(self):
        deg = self.degree
        if self.symbolic.is_polynomial():
            return {1: 'linear', 2: 'quadratic', 3: 'cubic'}.get(deg, 'polynomial')
        if self.symbolic.is_rational_function():
            return 'rational'
        return 'other'


@dataclass(frozen=True)
class System:
    equations: tuple[Equation, ...]

    def solve(self, *symbols):
        exprs = [eq.expr for eq in self.equations]
        return sp.solve(exprs, *symbols)

    def latex(self):
        return sp.latex(sp.Eq(0, 0, evaluate=False, *[eq.expr for eq in self.equations]))


class SystemOfEquationsOld:
    def __init__(self, *eqs: Equation):
        self.eqs = eqs

    def solve_by_substitution(self):
        ...

    def solve_by_elimination(self):
        ...

    def solve_by_graphing(self):
        ...

class LinearEquation(Equation, LinearMixin):
    """Represents a linear equation in two variables."""
    def __init__(self, lhs, rhs):
        super().__init__(lhs, rhs)
        if self.degree != 1:
            raise ValueError("LinearEquation can only represent linear equations.")

class LinearEquationOld(Equation):
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


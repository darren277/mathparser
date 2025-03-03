""""""
from src.mathtokens import *

case_dict = {'+': Add, '-': Sub, '*': Mult, '/': Div, '=': Equal, 'mi': Identifier, 'mn': Number}


class ParseTree:
    def __init__(self, *math_tokens: MathToken):
        self.math_tokens = list(math_tokens)

    def walk(self, visitor):
        visitor.visit_ParseTree(self)

    def build_from_mathml(self, xml_string: str):
        raise Exception('Not implemented yet.')

    def build_from_latex(self, latex_string: str):
        raise Exception('Not implemented yet.')




class Visitor:
    def __init__(self):
        self.result = ''

    def visit_ParseTree(self, visited: ParseTree):
        for math_token in visited.math_tokens:
            self.result += math_token.accept(self)

    def visit_Number(self, visited: Number):
        return str(visited)

    def visit_Add(self, visited: Add):
        return str(visited)

    def visit_Sub(self, visited: Sub):
        return str(visited)

    def visit_Mult(self, visited: Mult):
        return str(visited)

    def visit_Div(self, visited: Div):
        return str(visited)

    def visit_Fraction(self, visited: Fraction):
        return str(visited)

    def visit_Summation(self, visited: Summation):
        return str(visited)


class LatexVisitor(Visitor):
    def visit_Operation(self, visited: Operation):
        # Return Tokenized...?
        return str(visited)

    def visit_Fraction(self, visited: Fraction):
        # Return Tokenized...?
        return f'\\frac{{{visited.numerator.accept(self)}}}{{{visited.denominator.accept(self)}}}'

    def visit_Summation(self, visited: Summation):
        # Return Tokenized...?
        return f'\\sum_{{{visited.lower_limit.accept(self)}}}^{{{visited.upper_limit.accept(self)}}}{{{visited.body.accept(self)}}}'



class MathMLVisitor(Visitor):
    def visit_Operation(self, visited: Operation):
        # Return Tokenized...?
        return str(visited)

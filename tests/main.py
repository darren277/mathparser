""""""

import unittest

from bs4 import BeautifulSoup

latex_string = r"""
X_k
 = \frac{1}{2} (x_0 + (-1)^k x_{N-1}) 
 + \sum_{n=1}^{N-2} x_n \cos \left[\, \frac{\pi}{\,N-1\,} \, n \, k \,\right]
 \qquad \text{ for } ~ k = 0,\ \ldots\ N-1 ~.
"""

fetch_from_wikipedia = lambda page, section_id: BeautifulSoup(open(f'tests/mocks/dct.html', 'r', encoding='utf-8').read())


# \frac{1}{2} (x_0 + (-1)^k x_{N-1})

# \sum_{n=1}^{N-2} x_n \cos \left[\, \frac{\pi}{\,N-1\,} \, n \, k \,\right]


class Testing(unittest.TestCase):
    def test_parse_latex_simple(self):
        from pylatexenc.latexwalker import LatexWalker, LatexGroupNode, LatexMacroNode, LatexCharsNode
        latex_case_dict = {
            LatexCharsNode: lambda node: f"CharsNode: {node.latex_verbatim()}",
            LatexMacroNode: lambda node: f"MacroNode: {node.macroname}",
            LatexGroupNode: lambda node: f"GroupNode: {node.latex_verbatim()}"
        }
        ww = LatexWalker(r'x = \frac{1}{2}')
        (nodelist, pos, len_) = ww.get_latex_nodes(pos=0)
        for node in nodelist:
            print(node.latex_verbatim())
            print(latex_case_dict[type(node)](node))
            # TODO: test parsing of latex.

    def test_parse_mathml_simple(self):
        s = '<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>+</mo><mn>1</mn></math>'
        #from src.parser import ParseTree
        #parsed = ParseTree().build_from_mathml(s)
        #print(parsed.math_tokens[0].left, parsed.math_tokens[0].right)

    def test_evaluate_mathml(self):
        # TODO: test evaluation of parsed mathml.
        ...

    def test_evaluate_latex(self):
        # TODO: test evaluation of parsed latex.
        ...

    def test_parse_mathml_dct(self):
        return True if True else fetch_from_wikipedia('Discrete_cosine_transform', 'DCT-I')

    def test_parse_latex_dct(self):
        tex = fetch_from_wikipedia('Discrete_cosine_transform', 'DCT-I').find('annotation', {'encoding': 'application/x-tex'}).text
        from src.parser import ParseTree
        #parsed = ParseTree().build_from_latex(tex)
        ...

    def test_math2py_build(self):
        from src.mathtokens import Add, Number, Mult
        from src.parser import ParseTree, Visitor
        expr = Add(Number(1), Mult(Number(2), Number(2)))
        tree = ParseTree(expr)
        visitor = Visitor()
        tree.walk(visitor)
        assert str(visitor.result) == '1+2*2'

    def test_math2py_build_order_of_operations(self):
        # TODO: test order of operations.
        ...


    def test_math2py_parse(self):
        expr = ''


if __name__ == '__main__':
    unittest.main()



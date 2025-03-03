""""""


class MathToken:
    def accept(self, visitor):
        raise NotImplementedError
        #return visitor.visit_math_token(self)


class Number(MathToken):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def accept(self, visitor):
        return visitor.visit_Number(self)


class Identifier(MathToken):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)

    def mathml(self):
        return f'<mi>{self.name}</mi>'

    def accept(self, visitor):
        return visitor.visit_Identifier(self)



class Operation(MathToken):
    _symbol: str
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.left} {self._symbol} {self.right}'

    def mathml(self):
        return f'<mrow>{self.left.mathml()}{self._symbol}{self.right.mathml()}</mrow>'

    def accept(self, visitor):
        return self._symbol.join([self.left.accept(visitor), self.right.accept(visitor)])




class Add(Operation):
    _symbol = '+'

class Sub(Operation):
    _symbol = '-'

class Mult(Operation):
    _symbol = '*'

class Div(Operation):
    _symbol = '/'

class Equal(Operation):
    _symbol = '='



class Fraction(MathToken):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f'({self.numerator}/{self.denominator})'

    def mathml(self):
        return f'<mfrac>{self.numerator.mathml()}{self.denominator.mathml()}</mfrac>'

    def accept(self, visitor):
        return visitor.visit_Fraction(self)




class Summation(MathToken):
    def __init__(self, lower_limit, upper_limit, body):
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.body = body

    def __str__(self):
        return f'Sum({self.lower_limit}, {self.upper_limit}, {self.body})'

    def mathml(self):
        return f'<msubsup><mo>&#x2211;</mo><mrow>{self.lower_limit.mathml()}{self.upper_limit.mathml()}</mrow><mrow>{self.body.mathml()}</mrow></msubsup>'

    def accept(self, visitor):
        return visitor.visit_Summation(self)



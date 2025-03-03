.ONESHELL:

activate:
	.\venv\Scripts\activate

test: activate
	python -m unittest 'tests/main.py' -v

run: activate
	python main.py '<mi>1</mi><mo>+</mo><mn>1</mn>' --mathml 'y'

run2: activate
	python main.py 'x = \frac{1}{2}' --latex 'y'


# append to path C:\Users\Darren\AppData\Local\Programs\MiKTeX\miktex\bin\x64

PATH := $(PATH);C:\Users\Darren\AppData\Local\Programs\MiKTeX\miktex\bin\x64

viz1:
	manim -p -ql src/viz/main.py SquareToCircle

viz2:
	manim -p -ql src/viz/main.py MovingFrameBox


logviz-quotient-rule:
	manim -p -ql src/viz/main.py LogarithmQuotientRule

logviz-product-rule:
	manim -p -ql src/viz/main.py LogarithmProductRule

logviz-power-rule:
	manim -p -ql src/viz/main.py LogarithmPowerRule

logviz-eq1:
	manim -p -ql src/viz/main.py LogarithmEquation1

logviz-eq2:
	manim -p -ql src/viz/main.py LogarithmEquation2

logviz-eq3:
	manim -p -ql src/viz/main.py LogarithmEquation3


logviz-quotient-example:
	manim -p -ql src/viz/main.py LogQuotientRuleAndExample

logviz-product-example:
	manim -p -ql src/viz/main.py LogProductRuleAndExample

logviz-power-example:
	manim -p -ql src/viz/main.py LogPowerRuleAndExample

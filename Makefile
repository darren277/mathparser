.ONESHELL:

activate:
	.\venv\Scripts\activate

test: activate
	python -m unittest 'tests/main.py' -v

run: activate
	python main.py '<mi>1</mi><mo>+</mo><mn>1</mn>' --mathml 'y'

run2: activate
	python main.py 'x = \frac{1}{2}' --latex 'y'

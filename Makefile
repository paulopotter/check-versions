run:
	python run.py

test:
	@PYTHONPATH=.:.. py.test -k tests/ -s

dependencies:
	pip install -r requirements.txt

developer:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

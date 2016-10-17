run:
	python run.py

test:
	@PYTHONPATH=.:.. py.test -k tests/ -s

dependencies:
	pip install -r requirements.txt

developer:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

# watch: # # dont working / only on terminal
# 	scss --watch static/scss/:static/css/

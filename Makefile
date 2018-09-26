# Makefile executes first target if all is not specified
init:
	pip install pipenv --upgrade
	pipenv install

test:
	scripts/ci

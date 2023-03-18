PIP_COMPILE_FLAGS = -U --generate-hashes --build-isolation --allow-unsafe --resolver=backtracking
PYTHON_SOURCES = 040-decorators/*.py 050-exceptions/*.py 060-logging/*.py 060-logging/submodule/*.py
default: check

check: black-check flake8 mypy pytest isort-check

fmt: black isort

black:
	black $(PYTHON_SOURCES)

black-check:
	black --check --diff $(PYTHON_SOURCES)

flake8:
	flake8 $(PYTHON_SOURCES)

isort:
	isort $(PYTHON_SOURCES)

isort-check:
	isort --check --diff $(PYTHON_SOURCES)

mypy:
	mypy $(PYTHON_SOURCES)

pytest:
	pytest -v --color=yes --durations=20 --doctest-modules $(PYTHON_SOURCES)

clean:
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	find -type d -name '__pycache__' | xargs --no-run-if-empty rm -rf

cleanall: clean
	rm -rf venv

requirements:
	pip install -U pip-tools
	@echo "# Please seat back and relax, this may take some time. :)"
	pip-compile $(PIP_COMPILE_FLAGS) -o requirements.txt requirements.in
	pip-compile $(PIP_COMPILE_FLAGS) -o requirements-dev.txt requirements-dev.in

.PHONY: default fmt check black black-check flake8 mypy pytest docs rtfm requirements

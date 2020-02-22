VIRTUAL_ENV ?= venv
PIP=$(VIRTUAL_ENV)/bin/pip
PYTHON=$(VIRTUAL_ENV)/bin/python
PYTHON_VERSION=3.7
PYTHON_WITH_VERSION=python$(PYTHON_VERSION)

clean:
	@rm -rf $(VIRTUAL_ENV)/
	@find . -name *.pyc -delete
	@find . -name *__pycache__ -delete

$(VIRTUAL_ENV):
	virtualenv --python=$(PYTHON_WITH_VERSION) $(VIRTUAL_ENV)/
	$(PIP) install -r requirements-dev.txt

virtualenv: $(VIRTUAL_ENV)

pin-requirements:
	$(PIP) freeze > requirements.txt

start:
	$(PYTHON) mysite/manage.py runserver

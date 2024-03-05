NAME := fip11
INSTALL_STAMP := .install.stamp
POETRY := $(shell command -v poetry 2> /dev/null)

.DEFAULT_GOAL := help

define install_poetry
	if ! command -v poetry &> /dev/null; then \
    	pip install --upgrade pip; \
		pip install poetry; \
	else \
    	echo "Poetry is already installed."; \
	fi
endef

.PHONY: help
help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo ""
	@echo "  install     install packages and prepare environment"
	@echo "  clean       remove all temporary files"
	@echo "  lint        run the code linters"
	@echo "  format      reformat code"
	@echo "  test        run all the tests"
	@echo ""
	@echo "Check the Makefile to know exactly what each target is doing."

install: $(INSTALL_STAMP)
$(INSTALL_STAMP): 
	$(call install_poetry) && \
	$(POETRY) install

.PHONY: clean
clean:
	find . -type d -name "__pycache__" | xargs rm -rf {};

.PHONY: lint
lint: 
	$(POETRY) run isort --profile=black --lines-after-imports=2 --check-only ./tests/ $(NAME)
	$(POETRY) run black --check ./tests/ $(NAME) --diff
	$(POETRY) run flake8 --ignore=W503,E501 ./tests/ $(NAME)
	$(POETRY) run mypy ./tests/ $(NAME) --ignore-missing-imports
	$(POETRY) run bandit -r $(NAME) -s B608

.PHONY: format
format: $(INSTALL_STAMP)
	$(POETRY) run isort --profile=black --lines-after-imports=2 ./tests/ $(NAME)
	$(POETRY) run black ./tests/ $(NAME)

.PHONY: test
test: $(INSTALL_STAMP)
	$(POETRY) run pytest ./tests/ --cov-report term-missing --cov-fail-under 100 --cov $(NAME)
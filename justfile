.ONESHELL:

alias t := test
alias i := install

create:
    conda env -f conda.yaml

install:
    conda install -f conda.yaml

set shell := ["bash", "-uc"]

test:
    python -m pytest --cov=models/ --cov-report term-missing
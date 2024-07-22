alias t := test
alias i := install
alias c := create

set shell := ["bash", "-uc"]

create:
    conda env create -f conda.yaml

install:
    conda install -f conda.yaml

test:
    python -m pytest --cov=models/ --cov-report term-missing
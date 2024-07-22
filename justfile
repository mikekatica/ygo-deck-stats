alias t := test
alias i := install
alias c := create

set shell := ["bash", "-uc"]

create:
    conda env create -f conda.yaml

install:
    conda activate env
    conda install --yes matplotlib scipy pytest pytest-cov ipython ipykernel
    pip install pytest-notebook

configure:
    conda activate env
    ipython kernel install --name "python3" --user

test:
    conda activate env
    python -m pytest --cov=models/ --cov-report term-missing
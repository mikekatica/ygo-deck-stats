alias t := test
alias i := install

install:
    conda install --yes matplotlib scipy

test: install
    conda install --yes pytest pytest-cov
    pip install pytest-notebook
    python -m pytest --cov=models/ --cov-report term-missing
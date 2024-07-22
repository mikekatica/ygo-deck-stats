alias t := test
alias i := install

install:
    conda install matplotlib scipy

test: install
    conda install pytest pytest-cov
    pip install pytest-notebook
    python -m pytest
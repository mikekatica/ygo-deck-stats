alias t := test
alias i := install

install:
    conda install matplotlib scipy

test: install
    conda install pytest pytest-cov
    pip install pytest-notebook
    ipython -c "%run ygo_probabilities.ipynb"
    python -m pytest
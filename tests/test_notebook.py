from pytest_notebook.execution import execute_notebook
from pytest_notebook.notebook import load_notebook
from os.path import join
from pathlib import Path

def test_nb():
    p = Path(__file__)
    nb = join(p.parent, "../ygo_probabilities.ipynb")
    result = execute_notebook(load_notebook(nb))
    assert True
from pytest_notebook.nb_regression import NBRegressionFixture
from os.path import join
from pathlib import Path

def test_nb():
    fixture = NBRegressionFixture(exec_timeout=50)
    fixture.diff_color_words = False
    p = Path(__file__)
    nb = join(p.parent, "..\ygo_probabilities.ipynb")
    result = fixture.check(nb)
    print(result)
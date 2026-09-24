import pytest

@pytest.mark.regression
def test_regression():
    print("Test1")

@pytest.mark.xfail
def test_regression1():
    print("test2")
    assert 4 == 5

# to run excluding marked TC: py -m pytest -v -m "not regression"
# to run only the marked TC: py -m pytest -v -m regression
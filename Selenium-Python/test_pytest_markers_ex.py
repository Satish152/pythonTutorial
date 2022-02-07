import pytest


@pytest.mark.sanity
def test1():
    print("this is sanity test")

@pytest.mark.regression
def test2():
    print("This is Regression")

@pytest.mark.sanity
def test3():
    print("this is Sanity test 2")

@pytest.mark.smoke
def test4():
    print("This is smoke test")
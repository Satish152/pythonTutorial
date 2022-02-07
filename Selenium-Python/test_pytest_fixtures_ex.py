# fixture annotayion is used to execute the method before executinh any test methods in a test set
# we can set the after execution configuration by defining the code after yield keyword
#  after creting the test methods, we can pass the fixture method in to test method as a parameter
# when we execute this, setup method will execute first then it executes the remaining test methof

import pytest

@pytest.fixture
def setup():
    print("open browser")
    print("navigate to shopping site")
    print("search for product")
    yield
    print("log off from the account")
    print("close the browser")

def test_make_order(setup):
    print("make you order")

def test_remove_order(setup):
    print("place order")
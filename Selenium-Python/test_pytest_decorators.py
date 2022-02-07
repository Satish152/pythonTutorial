import pytest

@pytest.mark.skip
def test_skip_test_ex():
    print("this test will skip")

@pytest.mark.xfail
def test_expected_fail_ex():
    print("This test is expected to fail")

@pytest.mark.sanity
def test_sanity():
    print("sanity test")

@pytest.mark.regression
def test_regression():
    print("regression test")

@pytest.mark.tryfirst
def test_try_first_ex():
    print("try first example")
# Pytest filename should start or end with "test_*.py" or "*_test.py"
# method name should start with "test_"
# for Pytest we need to set the run configuration
# Edit Configuration -> Select Python test section -> click on "+" icon -> browse the test file -> click ok

def test_login():
    print("login Successful")

def test_message():
    print("message sent")

def test_logout():
    print("logoff done")
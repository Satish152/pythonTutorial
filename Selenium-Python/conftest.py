#conftest.py is the file which is automatically identify by pytest, which contains all the common and
# reusable function that can be directly accessible once we define it in the conftest.py file

#if there is a multipe number of functions or modules or classes that we need to use conftest then
# we can use the feature available in conftest called "autouse=True" and "scope="
# autouse - by the name itself we got that fixture method is execute automatically
# scope= is defined the scope of fixture function which we can define at what stage it can execute
#Ex: module, function, class,package,session

import pytest


@pytest.fixture(autouse=True,scope="module")
def setup():
    print("open browser")
    print("navigate to shopping site")
    print("search for product")
    yield
    print("log off from the account")
    print("close the browser")
#conftest.py is the file which is automatically identify by pytest, which contains all the common and
# reusable function that can be directly accessible once we define it in the conftest.py file

#def test_add_items(setup):
#    print("items added")

#def test_remove_item(setup):
#    print("items removed")

#if there is a multipe number of functions or modules or classes that we need to use conftest then
# we can use the feature available in conftest called "autouse=True" and "scope="
# autouse - by the name itself we got that fixture method is execute automatically
# scope= is defined the scope of fixture function which we can define at what stage it can execute
#Ex: module, function, class,package,session

#By default scope of conftest is defined for functions
def test_add_items():
    print("items added")

def test_remove_item():
    print("items removed")
import pytest


# We can create setup and teardown methods using the fixture tag- these are created in a conftest.py file, which
#  allows them to be imported into any test files that need them. First, we specify the pre-requisites and then
# pass the name of the method (setup in this instance) into other methods that we want to associate it with, as
# an argument. In the same method, we then use the yield statement, and then specify the teardown steps. So, the
# order of events will be as follows:
# 1) Setup/pre-requisite steps will run - e.g. opening and configuring browser
# 2) The other test methods associated with it will run - example in test_demo.py
# 3) The teardown steps (specified after the yield statement) will run - e.g. closing browser and deleting cookies
# The scope='class' argument specifies that we will be applying this at class level (only if the test cases are in
# a class; not needed if they are just separate methods). This allows the fixture to only be run once before the
# relevant class is initialised, and then again to tear down once all the relevant tests have run
@pytest.fixture(scope='class')
def setup():
    """
    This test will run the pre-requisites, and then the teardown steps after the yield statement
    """
    print('I will be executed first')
    yield
    print('I will be executed last')


@pytest.fixture()
def data_load():
    """
    This fixture return user registration data as a list and will be inherited by the TestExampleTwo test
    in test_fixtures_data.py. This is an example of us using a data driven fixture
    """
    print('User profile data is being created')
    return ["Rahul", "Shetty", "rahulshettyacademy.com"]


# With this fixture, we are passing in various parameters that we want to use in each cycle of the tests. In this
# example, we pass in the various browsers as parameters. The first cycle of tests will us the Chrome param, the
# the tests will then repeat using the Firefox param in the second cycle, and so on. This fixture will be passed
# into the test_cross_browser test case in test_fixtures_data.py file
# *** To pass in multiple params in the same run, we can do so in a tuple - the first tuple includes all the params
# that will be passed in on the first run ***
@pytest.fixture(params=[("Chrome", "Sunny", "Hebbar"), "Firefox", "IE"])
def cross_browser(request):
    """
    This fixture takes the request parameter to retrieve the params from the fixture decorator and then pass
    them into the method itself. It is called in the method using request.param
    """
    return request.param

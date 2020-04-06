# Any pytest file should start with test_ or end with _test
# Any method should start with test_
# To run the tests in the terminal, we use cd into the directory and use the "py.test -v -s" command
# This command runs all the test files in the directory
# To run a particular file - "py.test test_file_name.py -v -s"
# To only run particular tests, use the regex (-k) flag - "py.test -k the_same -v -s"
# This will only run tests from all files that have "the_same" in their method name
import pytest


# If we want to mark particular tests as part of the same group, we use @pytest.mark, followed by the name
# we want to give the group. We apply this to all the relevant tests in our files that we want to belong to the
# same group. Then, to only run those cases, we run the command - "pytest.py -m group_name -v -s
# The preferred method is to use the -k tag (explained above)
@pytest.mark.smoke
# To skip a particular test, use the mark.skip tag
@pytest.mark.skip
# To run the test but not include it in the test report, use the mark.xfail tag
@pytest.mark.xfail
def test_hello_world():
    print("Hello World")


def test_num_is_the_same():
    # The second argument gets printed if the test fails
    assert 2 == 2, "Test failed because numbers aren't the same"


# We can create setup and teardown methods using the fixture tag. First, we specify the pre-requisites and then
# pass the name of the method (setup in this instance) into other methods that we want to associate it with, as
# an argument. In the same method, we then use the yield statement, and then specify the teardown steps. So, the
# order of events will be as follows:
# 1) Setup/pre-requisite steps will run - e.g. opening and configuring browser
# 2) The other test methods associated with it will run
# 3) The teardown steps (specified after the yield statement) will run - e.g. closing browser and deleting cookies
@pytest.fixture()
def setup():
    """
    This test will run the pre-requisites, and then the teardown steps after the yield statement
    """
    print('I will be executed first')
    yield
    print('I will be executed last')


def test_fixtureDemo(setup):
    """
    This test will be linked to the setup fixture and will run before any other tests
    """
    print('I will execute before all tests')

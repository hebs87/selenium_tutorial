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


# Linked to the setup fixture in the conftest.py file - no need to import it in, as pytest will automatically pick it up
# Declaring the fixture in the mark.usefixtures tag directly above a class declaration will allow us the class to
# inherit it, and it will be applied to all methods of that class, instead of having to call it in each method
@pytest.mark.usefixtures('setup')
class TestExample:
    def test_fixture_demo(self):
        """
        This test will be linked to the setup fixture and will run before any other tests
        """
        print('I will execute before all tests')

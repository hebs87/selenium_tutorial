import pytest


@pytest.mark.usefixtures('data_load')
class TestExampleTwo:
    # As we are returning data in the fixture, we need to pass the fixture name into the method as a parameter
    def test_edit_profile(self, data_load):
        """
        A test that uses the data from the fixture and then displays the various values
        """
        print('First Name: ' + data_load[0])
        print('Surname: ' + data_load[1])
        print('Website: ' + data_load[2])


def test_cross_browser(cross_browser):
    """
    This test uses the cross_browser fixture. As the fixture passes in 3 parameters, the test runs 3 times:
    1) Prints "Chrome"
    2) Prints "Firefox"
    3) Prints "IE"
    """
    print(cross_browser)

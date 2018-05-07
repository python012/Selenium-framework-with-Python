
'''
Setup/teardown with pytest, see https: // docs.pytest.org/en/3.5.1/xunit_setup.html

Remarks:
1. It is possible for setup/teardown pairs to be invoked multiple times per testing process.
2. teardown functions are not called if the corresponding setup function existed and failed/was skipped.
'''

import pytest

def setup_module(module):
    """
    setup any state specific to the execution of the given module."""
    print()
    print("-------------- setup before module --------------")


def teardown_module(module):
    """ teardown any state that was previously setup with a setup_module
    method.
    """
    print("-------------- setup after module --------------")


class TestBaidu(object):

    def test_login(self):
        print("test baidu login function")
        assert True == True


class TestSohu(object):

    @classmethod
    def setup_class(cls):
        """ setup any state specific to the execution of the given class (which 
        usually contains tests).
        """
        print("------ setup before class TestSohu ------")

    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        print("------ teardown after class TestSohu ------")

    def setup_method(self, method):
        print("--- setup before each method ---")
    
    def teardown_method(self, method):
        print("--- teardown after each method ---")

    def test_login(self):
        print("sohu login")
        assert True == True

    def test_logout(self):
        print("sohu logout")
        pytest.skip()

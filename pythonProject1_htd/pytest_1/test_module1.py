import pytest

'''
@pytest.fixture(autouse="True")
def greet():
    print("****hi****")     #set up module
    yield
    print("****bye****")    #teardown module


def test_spam(greet):
    print("in test spam")



def test_display(greet):
    print("in diaplay")

'''

@pytest.fixture(autouse="True", scope="class")
def greet():
    print("****hi****")     #set up module
    yield
    print("****bye****")    #teardown module



@pytest.mark.usefixtures("greet")
class TestDemo:
    def test_spam(self):
        print("in test spam")



    def test_display(self):
        print("in diaplay")










































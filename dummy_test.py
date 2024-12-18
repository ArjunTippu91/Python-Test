'''This is simple unit test comparison
'''
# pylint: disable=C0116
# pylint: disable=W0105
def capital_case(x):
    return x.capitalize()

'''Assertion
'''
def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

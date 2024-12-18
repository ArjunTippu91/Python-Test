'''This is simple unit test comparison
'''
def capital_case(x):
    return x.capitalize()

'''Assertion
'''
def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

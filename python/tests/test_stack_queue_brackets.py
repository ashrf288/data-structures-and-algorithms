from challenges.stack_queue_brackets.stack_queue_brackets import validate_brackets


def test_cas1():
    #input
    value='{}'

    #output
    expected=True
    actul=validate_brackets(value)
    assert expected==actul
def test_cas2():
    #input
    value='{}(){}'

    #output
    expected=True
    actul=validate_brackets(value)
    assert expected==actul
def test_cas3():
    #input
    value='()[[Extra Characters]]'

    #output
    expected=True
    actul=validate_brackets(value)
    assert expected==actul
def test_cas4():
    #input
    value='(){}[[]]'

    #output
    expected=True
    actul=validate_brackets(value)
    assert expected==actul
def test_cas5():
    #input
    value='{}{Code}[Fellows](())'

    #output
    expected=True
    actul=validate_brackets(value)
    assert expected==actul
def test_cas6():
    #input
    value='[({}]'

    #output
    expected=False
    actul=validate_brackets(value)
    assert expected==actul
def test_cas7():
    #input
    value='(]('

    #output
    expected=False
    actul=validate_brackets(value)
    assert expected==actul

def test_cas8():
    #input
    value='{(})'

    #output
    expected=False
    actul=validate_brackets(value)
    assert expected==actul

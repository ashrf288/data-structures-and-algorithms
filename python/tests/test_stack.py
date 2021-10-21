from challenges.stack_and_queue.stack import Stack
import pytest

   
@pytest.fixture
def stack():
    pass


def test_push_stack():
    stack=Stack()
    stack.push(1)

    #output
    expected=1
    actul=stack.top.data
    assert expected==actul
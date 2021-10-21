from challenges.stack_and_queue.stack import Stack
import pytest

   
@pytest.fixture
def stack():
   stack=Stack()
   return stack


def test_push_stack(stack):
    #input
    stack.push(1)

    #output
    expected=1
    actul=stack.top.data
    assert expected==actul

def test_pushMultiple(stack):
      #input
    stack.push(1)
    stack.push(2)
    stack.push(3)
      #output
    expected=3
    actul=stack.top.data
    assert expected==actul
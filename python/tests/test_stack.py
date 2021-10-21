from challenges.stack_and_queue.stack import Stack
import pytest

   
@pytest.fixture
def stack():
   stack=Stack()
   stack.push(1)
   stack.push(2)
   stack.push(3)
  
   return stack


def test_push_stack(stack):
    #output
    expected=3
    actul=stack.top.data
    assert expected==actul

def test_pushMultiple(stack):
      #output
    expected=3
    actul=stack.top.data
    assert expected==actul

def test_pop1(stack):
      #input
    stack.pop()
    #output
    expected=3
    actul=stack.pop()
    assert expected==actul

def test_pop2(stack):
      #input
    stack.pop()
    stack.pop()
    stack.pop()
    #output
    expected=True
    actul=stack.is_empty()
    assert expected==actul

def test_peek(stack):
      #output
    expected=2
    actul=stack.peek()
    assert expected==actul

def test_initate_stack():
    #INPUT
    stack=Stack()
     #output
    expected=True
    actul=stack.is_empty()
    assert expected==actul

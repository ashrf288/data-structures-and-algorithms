from challenges.stack_and_queue.queue import Queue
import pytest


@pytest.fixture
def queue():
    queue=Queue()
    queue.enqueue(1)
    return queue

def test_enqueue(queue):
    #output
    actul=1
    expected=queue.front.data
    assert  actul==expected

def test_enqueue2(queue):
    queue.enqueue(2)
    queue.enqueue(3)
    #output
    actul=3
    expected=queue.rear.data
    assert  actul==expected

def test_dequeue(queue):
    #output
    actul=1
    expected=queue.dequeue()
    assert  actul==expected

def test_peek(queue):
    #output
    actul=1
    expected=queue.peek()
def test_dequeue(queue):
    with pytest.raises(Exception):
        queue.enqueue(2)
        queue.enqueue(3)
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()


def test_emptyQueue():
    queue=Queue()

    expected=True
    actul=queue.is_empty()
    assert expected==actul

   

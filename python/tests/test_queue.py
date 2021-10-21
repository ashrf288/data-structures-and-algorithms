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
    queue.enqueue(2)
    queue.enqueue(3)
    #output
    actul=1
    expected=queue.dequeue()
    assert  actul==expected
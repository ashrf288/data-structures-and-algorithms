from challenges.stack_and_queue.queue import Queue
import pytest


@pytest.fixture
def queue():
    queue=Queue()
    return queue

def test_enqueue(queue):
    queue.enqueue(1)
    #output
    actul=1
    expected=queue.front.data
    assert  actul==expected

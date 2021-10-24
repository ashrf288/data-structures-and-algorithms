from challenges.pseudo_queue.pseudo_queue import Pseudo_queue


def test_psudo_enqueue():
    queue=Pseudo_queue()
    queue.enqueue(1)
    #output
    actul=1
    expected=queue.front.data
    assert  actul==expected

def test_psudo_dequeue():
    queue=Pseudo_queue()
    queue.enqueue(1)
    
    #output
    actul=1
    expected=queue.dequeue()
    assert  actul==expected

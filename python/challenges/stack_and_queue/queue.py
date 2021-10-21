from challenges.stack_and_queue.node import Node


class Queue :
    def __init__(self,front=None,rear=None):
        self.front=front
        self.rear=rear
    def enqueue(self,value):
        '''
        adds a new node with that value to the back of the queue with an O(1) Time performance.
        '''

        node =Node(value)
        self.rear.next=None
        self.rear=node 
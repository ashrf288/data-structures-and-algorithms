from challenges.stack_and_queue.node import Node
from challenges.stack_and_queue.stack import Stack


class Pseudo_queue:
     def __init__(self,front=None,rear=None):
        self.front=front
        self.rear=rear
        self.inbox=Stack()
        self.outbox=Stack()
 
     def enqueue(self):
         pass

     def dequeue(self):
         pass

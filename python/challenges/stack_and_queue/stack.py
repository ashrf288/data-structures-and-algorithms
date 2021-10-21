from node import Node


class Stack:
    def __init__(self,top=None) :
        self.top=top
    

    def push(self,value):
        '''
        adds a new node with that value to the 
        top of the stack with an O(1) Time performance.
        '''
        node =  Node(value)
        node.next=self.top
        self.top=node

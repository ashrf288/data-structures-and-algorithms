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


    def pop(self):
        '''
        Removes the node from the top of the stack
        Should raise exception when called on empty stack
        '''
        if not self.is_empty():
           removed_node=self.top
           self.top=self.top.next
           self.top.next=None
           return removed_node
        else:
            raise Exception ('node is empty')

    def is_empty(self):
        if self.top==None:
            return True
        else:
            return False
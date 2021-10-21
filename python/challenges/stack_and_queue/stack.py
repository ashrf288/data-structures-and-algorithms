from challenges.stack_and_queue.node import Node


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

    def is_empty(self):
        '''
        Returns: Boolean indicating whether or not the stack is empty.
        '''
        if self.top==None:
            return True
        else:
            return False

    def pop(self):
        '''
        Removes the node from the top of the stack
        Should raise exception when called on empty stack
        '''
        if not self.is_empty():
           removed_node=self.top
           self.top=self.top.next
           removed_node.next=None
           return removed_node.data
        else:
            raise Exception ('node is empty')
    
    def peek(self):
        '''
        Returns: Value of the node located at the top of the stack
        Should raise exception when called on empty stack
        '''
        if not self.is_empty():
           return self.top.next
        else:
            raise Exception ('node is empty')    



   
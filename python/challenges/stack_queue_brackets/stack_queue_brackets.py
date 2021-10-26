from challenges.stack_and_queue.node import Node


class Stack:
    def __init__(self):
        self.top=None
        self.size=0


    def is_empty(self):
        return self.size==0

    def push(self,data):
        self.top=Node(data,self.top)
        self.size +=1

    def pop(self):
        if self.is_empty(): 
            raise Exception("stack is empty")
        result=self.top.data  
        self.top=self.top.next 
        self.size -=1  
        return result

    def peek(self):
        if self.is_empty==0:
            raise Exception("stack is empty")
        return self.top.data




def validate_brackets(item:str):
    '''
    this function takes in string as input and returns a boolean
    it will loop though a string and push each value to the created stack
    if the value was an  openinig  barcit of any type 
    and if it was a closing bracit  then it will check for the peek for next charcter 
    and search if the next bracit is matching the value(i)   

    '''
    stack=Stack()
    for i in item:
        if i=="{" or i=="[" or i=="(":
            stack.push(i)
        elif i=="}":
            if stack.peek()=="{":
                stack.pop()
            else:
                return False
        elif i=="]":
            if stack.peek()=="[":
                stack.pop()
            else:
                return False
        elif i==")":
            if stack.peek()=="(":
                stack.pop()
            else:
                return False
    if stack.top:
        return False
    else:
        return True


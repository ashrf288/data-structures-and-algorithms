class Node:
 
  def __init__(self, data, next_ = None):
    self.data = data
    self.next = next_

    
class LinkedList:
 

  def __init__(self):
    self.head = None

  def insert(self, value):
   
    # create new node
    self.head = Node(value, self.head)
    return self.head 

  # def includes(self,value):
      
  def includes(self,value):
         
  #   Current <-- Head
      current=self.head
  # WHILE Current is not NULL
      while current != None:
  #   IF Current.Value is equal to value
        if current.data==value:
  #     return TRUE
           return True
  #   Current <-- Current.Next
        else:
          current=current.next
      
      return False


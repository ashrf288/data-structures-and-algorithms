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

  def toString(self):
   '''
  to string
Arguments: none
Returns: a string representing all the values in the Linked List,
 formatted as:
"{ a } -> { b } -> { c } -> NULL"

  '''
   string = ""
   current=self.head
  # WHILE Current is not NULL
   while current != None:
  #   IF Current.Value is equal to value
       value = current.data
       if current.next is None:
          string +="{"+f' {value} '+"}" + " -> NULL"
          break

       else:
          string +="{"+f' {value} '+"} -> "
          current = current.next
    #   Current <-- Current.Next
  #     return TRUE
   return string
      
  


ll=LinkedList()
ll.insert(1)
ll.insert(1)
ll.insert(1)

print(ll.toString())

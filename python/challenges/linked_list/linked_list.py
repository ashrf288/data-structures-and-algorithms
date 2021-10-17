class Node:
 
  def __init__(self, data, next_ = None):
    self.data = data
    self.next = next_

    
class LinkedList:
 

  def __init__(self):
    self.head = None

  def insert(self, value):

    '''
    takes in a value and insert this value with a refernce to the old head node abd push this value 
    to be the new head of linked list 
    '''   
    # create new node
    self.head = Node(value, self.head)
    return self.head 

  # def includes(self,value):
      
  def includes(self,value):
      '''
    returns a bollean if the nodes exiest in the linked list
     and false if not 
    '''
         
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

  def __str__(self):
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
   
  def append(self,value):
      '''
        this function will look for the nide that has node.next as none which
        will represnt the the last node then it will append the value(node)
        and it will give the new created node to that node .next
      '''
      current=self.head
      while current :
  #   IF Current.next is equal to none that means this is the last node 
        if current.next==None:
          
          current.next=Node(value)
          break
        current=current.next           
  #   Current <-- Current.Next
            
      
   
  


ll=LinkedList()
ll.insert(1)
ll.insert(1)
ll.insert(1)
ll.append(5)
print(str(ll))


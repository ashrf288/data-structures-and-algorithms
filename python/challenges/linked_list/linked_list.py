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
  

  def __iter__(self):
      """Tell Python that this class is iterable"""
      return self
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

            
      
  def append_multi(self,list):
    '''
    takes in s list of nodes and add them to the end of the 
    linked list 
    '''
    for item in list:
        self.append(item)
    return 'll' 


  def insertBefore(self, targetValue, value):
    # create new node
    newNode = Node(value)
    # find target node to insert
    node = self.head
    if node != None:
        # search nodes
        while node:
            if node.next == None:
                break
            if node.next.data == targetValue:
                newNode.next = node.next
                node.next = newNode
                break
            else:
                node = node.next

  def insert_after(self,value,new_value):
    current = self.head
    
    while current is not None:
        if current.data == value:
          newNode=Node(new_value,current.next)
          current.next=newNode
          break
        current = current.next  

  # @classmethod
  # def zipLists(cls,list1,list2):
  #      zip_ll=LinkedList()
  #      current = list1.head
  #      current2 = list2.head
  #      while current !=None:
  #        zip_ll.insert(current.data)
  #        zip_ll.insert(current2.data)
  #       #  zip_ll.insertBefore(i.next,)
  #        current=current.next

  #      return zip_ll  
      



ll=LinkedList()
ll.insert(1)
ll.insert(2)
ll2=LinkedList()
ll2.insert(3)
ll2.insert(4)
# ll.insert(3) 
# #  # ll.insert(1)
# #  # ll.append(5)
# # ll.insert(5)
# # ll.insert(4)
# # ll.append_multi([5,3,3])
# #  # ll.append_multi([5,3,2])
print(str(ll))  
ll.insert_after(1,22)
print(str(ll)) 


print(str(ll2)) 


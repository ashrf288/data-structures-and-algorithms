

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


class Queue:
  def __init__(self, collection=[]):
    self.data = collection

  def peek(self):
    if len(self.data):
      return True
    return False

  def enqueue(self,item):
    self.data.append(item)

  def dequeue(self):
    return self.data.pop(0)
class Binary_tree():

    def __init__(self):
        self.root=None
class Binary_search_tree(Binary_tree):
    
    def bfs(self):
     """
     A binary tree method which returns a list of items that it contains
     input: None
     output: tree items
    """
     breadth = Queue()
     breadth.enqueue(self.root)

     list_of_items = []
     while breadth.peek():
        front=breadth.dequeue()
        list_of_items+=[front.data]
        if front.left:
            breadth.enqueue(front.left)
        if front.right:
            breadth.enqueue(front.right)
     return list_of_items
    


class HashNode:
    def __init__(self, value=None, next_=None):
        """
      Initalization the Node
      """
        self.value = value
        self.next = next_


class LinkedList:
    def __init__(self):
        """
        The constructor method for the linked list. Initializes the head of a linked list to None.
        """
        self.head = None

    def insert(self, value):
        """
        Take a value and store it in a Node, then insert it to the beginning of the linked list.
        """
        self.head = HashNode(value, self.head)


class HashTable:
    def __init__(self, size=1024):
        """
        Initalization of Hash table
        
        """
        self.__size = size
        self.__buckets = [None] * size

    def __hash(self, key):
        """
        Takes a key which is a string and returns an integer which is the index that will be used to store the key/value pari in a Node at that index.
        """
        return sum([ord(char) for char in key]) * 7 % self.__size

    def add(self, key, value):
        """
        A method for adding a new value to the map
        This method should hash the key, and add the key and value pair to the table.

        Arg: Takes the key and value 
        Return : No return value
        """

        index = self.__hash(key)

        if not self.__buckets[index]:
          self.__buckets[index] = LinkedList()
        my_value = [key,value]
        self.__buckets[index].insert(my_value)
        return index

    def get(self, key):
        """
        Get the value corresponding to the key provided in the hashtable.
        Args:
            key (str): the key.
        Returns:
            any: the value stored corresponding to the key provided.
        """
        index = self.__hash(key)
     
        if self.__buckets[index]:

           linked_list = self.__buckets[index]
           current = linked_list.head
           while current:

                if current.value[0] == key: 
                   return current.value[1]
                current = current.next
        return None


def tree_intersection(bt1,bt2):
    '''
     `tree_intersection` that takes two binary trees as parameters.
    Using your Hashmap implementation as a part of your algorithm,
     return a set of values found in both trees.
    '''
    theData=[]
    intersections=[]
    ht = HashTable()
    bt1_data=bt1.bfs()
    bt2_data=bt2.bfs()
    for data in bt1_data:
        intersections.append(ht.add(data,data))
    for data in bt2_data:
        index=ht.add(str(data),data)
        if  index in intersections:
                theData.append(data)  
    return theData







def createTree():
    bt=Binary_search_tree()
    a_node = Node('1')
    b_node = Node('2')
    c_node = Node('3')
    d_node = Node('4')
    e_node = Node('5')
    f_node = Node('6')
    g_node = Node('7')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    b_node.right = e_node
    c_node.left = f_node
    c_node.right = g_node
    bt.root=a_node
    return bt

def createTree2():
    bt=Binary_search_tree()
    a_node = Node('1')
    b_node = Node('8')
    c_node = Node('8')
    d_node = Node('4')
    e_node = Node('5')
    f_node = Node('6')
    g_node = Node('7')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    b_node.right = e_node
    c_node.left = f_node
    c_node.right = g_node
    bt.root=a_node
    return bt

bt1=createTree()
bt2=createTree2()
print(bt1.bfs())
print(bt2.bfs())

print(tree_intersection(bt1,bt2))
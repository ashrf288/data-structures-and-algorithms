class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None



class Binary_tree():

    def __init__(self):
        self.root=None

    def pre_order(self):
      """
    A binary tree method which returns a list of items that it contains in (pre order) 
       root >> left >> right
    input: None

    output: tree items(list)
    we used the function (recur) to help with recursion inside the class
      """
      order=[]
      def recur(node):
          if node:
              order.append(node.data)
              if node.left:
                  recur(node.left)
              if node.right:
                  recur(node.right)    
      recur(self.root) 
      return order 


    def in_order(self):
      """
    A binary tree method which returns a list of items that it contains in (in order) 
       left >> root >> right
    input: None
    output: tree items(list)
    we used the function (recur) to help with recursion inside the class
      """
      order=[]
      def recur(node):
          if node:
              if node.left:
                  recur(node.left)
              order.append(node.data)
              if node.right:
                  recur(node.right)    
      recur(self.root) 
      return order      
    def post_order(self):
      """
    A binary tree method which returns a list of items that it contains in (post order) 
           left >> right >> root
    input: None
    output: tree items(list)
    we used the function (recur) to help with recursion inside the class
      """
      order=[]
      def recur(node):
          if node:
              if node.left:
                  recur(node.left)
              if node.right:
                  recur(node.right)   
              order.append(node.data) 
      recur(self.root) 
      return order      




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
    # while breadth.peek():
    #         front = breadth.dequeue()
    #         list_of_items += [front.data]

    #         if front.left:
    #          breadth.enqueue(front.left)

    #         if front.right:
    #          breadth.enqueue(front.right)

    # return list_of_items




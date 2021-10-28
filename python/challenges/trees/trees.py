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

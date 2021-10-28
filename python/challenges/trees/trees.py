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
    A binary tree method which returns a list of items that it contains

    input: None

    output: tree items

    sub method : walk () to make the recursion staff
      """
    # list_of_items = []
    # def walk(node):
    #   if node:
    #     list_of_items.append(node.data)
    #     if node.left:
    #       walk(node.left)
    #     if node.right:
    #       walk(node.right)

    #  walk(self.root)
    #  return list_of_items
      litsa=[]
      def recur(node):
          if node:
              litsa.append(node.data)
              print(node.left)
              if node.left:
                  recur(node.left)
              if node.right:
                  recur(node.right)    
      recur(self.root) 
      return litsa      

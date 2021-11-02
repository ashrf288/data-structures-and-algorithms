class Node():
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

class binary_tree():
    def __init__(self):
        self.root = None
        self.output = []

    def pre_order(self, root):
        # root >> left >> right
        pre_order_output=[]
        if root:
            pre_order_output.append(root.value)
            pre_order_output = pre_order_output + self.pre_order(root.left)
            pre_order_output = pre_order_output + self.pre_order(root.right)
        return pre_order_output
        
def fizzBuzz(node):
    '''
    If the value is divisible by 3, replace the value with “Fizz”
    If the value is divisible by 5, replace the value with “Buzz”
    If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
    If the value is not divisible by 3 or 5, simply turn the number into a String

    '''
    if node.value % 15 == 0:
        return'FizzBuzz'
    elif node.value %3 == 0:
        return'Fizz'
    elif node.value % 5 == 0:
        return'Buzz'
    else:
        return str(node.value)

def FizzBuzzTree(tree):
    '''
     Arguments: k-ary tree
      Return: new k-ary tree
      Determine whether or not the value of each node is divisible by 3, 5 or both.
     Create a new tree with the same structure as the original, 
    '''
    if not tree.root:
        return []
    new_binary_tree = binary_tree()
    def traverser(node):
        new_binary_tree.output = new_binary_tree.output + [fizzBuzz(node)]
        if node.left:           
            traverser(node.left)
        if node.right:
            traverser(node.right)
        return new_binary_tree.output
    return traverser(tree.root) 

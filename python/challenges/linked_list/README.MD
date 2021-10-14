
# Singly Linked List
<!-- Short summary or background information -->

## Challenge
<!-- Description of the challenge -->
Create a Linked List class

Within your Linked List class, include a `head` property.

Upon instantiation, an empty Linked List should be created.
The class should contain the following methods
`insert`
Arguments: value
Returns: nothing
Adds a new node with that value to the head of the list with an O(1) Time performance.
`includes`
Arguments: value
Returns: Boolean
Indicates whether that value exists as a Node’s value somewhere within the list.
`to string`
Arguments: none
Returns: a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
  linked list was used for this approch 
## API
<!-- Description of each method publicly available to your Linked List -->

###############################################
class Node:
  """
  A class representing a Node

  Attributes
  ----------


  Methods
  -------
  __init__(data, next_):
      the constructor method for the class, it takes two parameters, the data parameter is the a reference to the data the node will hold, and the next_ 

  """

  def __init__(self, data, next_ = None):
    self.data = data
    self.next = next_
###############################################################################

class LinkedList:
  """
  A class for creating instances of a Linked List.
  
  Data and other attributes defined here:
  
  head: Node | None

  Methods defined here

  insert(value: any)
  contains(value: any) -> bool
  """

  def __init__(self):
    self.head = None

  def insert(self, value):
    """"
    Insert creates a Node with the value that was passed and adds
    it to the head of the linked list shifting all other values down

    arguments:
    value : any

    returns: None
    """
    # create new node
    self.head = Node(value, self.head)  

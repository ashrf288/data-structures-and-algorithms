
# Singly Linked List
<!-- Short summary or background information -->


linked_list.py:

 [linked list .py](https://github.com/ashrf288/data-structures-and-algorithms/blob/linked-list/python/challenges/linked_list/linked_list.py)


 test_linked_list.py:
[test_linked list .py](/home/ashrf288/401/data-structures-and-algorithms/python/tests/test_linked_list.py)

pr link
[pull request](https://github.com/ashrf288/data-structures-and-algorithms/pull/25)

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
  linked list was used for this approch  as for the link list big o :
  ![](https://miro.medium.com/max/3000/1*3IlTLK_S0HmATuYQGxcbUA.png)
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
  ## __init__ 
  (data, next_):
      the constructor method for the class, it takes two parameters, the data parameter is the a reference to the data the node will hold, and the next_ 
   

## `insert`

Arguments: value

Returns: nothing

Adds a new node with that value to the head of the list with an O(1) Time performance.
 
## `includes`

Arguments: value

Returns: Boolean

Indicates whether that value exists as a Node’s value somewhere within the list.

## `to string`

Arguments: none

Returns: a string representing all the values in the Linked List, formatted as:

`"{ a } -> { b } -> { c } -> NULL"`

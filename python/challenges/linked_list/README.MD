
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


# lab 6 

# Challenge Summary
<!-- Description of the challenge -->

Write the following methods for the Linked List class:

`append`

arguments: new value

adds a new node with the given value to the end of the list

`insert before`

arguments: value, new value

adds a new node with the given new value immediately before the first node that has the value specified

`insert after`

arguments: value, new value

adds a new node with the given new value immediately after the first node that has the value specifie




## Whiteboard Process
<!-- Embedded whiteboard image -->






## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->


## Solution
<!-- Show how to run your code, and examples of it in action -->
[x]Can successfully add a node to the end of the linked list
[x]Can successfully add multiple nodes to the end of a linked list
[x]Can successfully insert a node before a node located i the middle of a linked list
[x]Can successfully insert a node before the first node of a linked list
[x]Can successfully insert after a node in the middle of the linked list
[x]Can successfully insert a node after the last node of the linked list



# lab 7 

##  Challenge Summary

`kth from end`
k-th value from the end of a linked list.


## Approach & Efficiency
![image](/python/assets/kth_elemnt.jpg)


## Solution

[x]argument: a number, k, as a parameter.
[x]Return the node’s value that is k places from the tail of the linked list.
[x]write unit tests


[x]Where k is greater than the length of the linked list
[x]Where k and the length of the list are the same
[x]Where k is not a positive integer
[x]Where the linked list is of a size 1
[x]“Happy Path” where k is not at the end, but somewhere in the middle of the linked list


## lab 8

# Challenge Summary


Write a function called `zip lists`
Arguments: 2 linked lists
Return: Linked List, zipped as noted below

`zipLists(list1, list2)`

      Arg  list1                         	Arg list2	                    
`head -> [1] -> [3] -> [2] ->`      `X	head -> [5] -> [9] -> [4] -> X`

      Output	
`head -> [1] -> [5] -> [3] -> [9] -> [2] -> [4] -> X`
## Approach & Efficiency

![white](https://github.com/ashrf288/data-structures-and-algorithms/blob/main/python/assets/whiteboard_zip.jpg)






## Solution

[x]Write a function called zip lists
[x]Arguments: 2 linked lists
[x]Return: Linked List, zipped as noted below
[x]Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list.
[x]Try and keep additional space down to O(1)
[x]You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

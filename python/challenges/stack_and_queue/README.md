
# Stacks and Queues
<!-- Short summary or background information -->
 

## Challenge
<!-- Description of the challenge -->
[x]Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.

## Stack


[x]Create a Stack class that has a top property. It creates an empty Stack when instantiated.
This object should be aware of a default empty value assigned to top when the stack is created.

[x]The class should contain the method push

[x]The class should contain the method pop

[x]The class should contain the method peek

[x]The class should contain the method is_empty


## Stack test ##
[x]Can successfully push onto a stack

[x]Can successfully push multiple values onto a stack

[x]Can successfully pop off the stack

[x]Can successfully empty a stack after multiple pops

[x]Can successfully peek the next item on the stack

[x]Can successfully instantiate an empty stack

[x]Calling pop or peek on empty stack raises exception


## queue

[x]Create a Queue class that has a front property. It creates an empty Queue when instantiated.

[x]This object should be aware of a default empty value assigned to front when the queue is created.

[x]enqueue dds a new node with that value to the back of the queue

[x]dequeue Returns: the value from node from the front of the queue Removes the node from the front of the queue
Should raise exception when called on empty queue

[x]peek : returns  Value of the node located at the front of the queue Should raise exception when called on empty stack

[x] is_empty: returns: Boolean indicating whether or not the queue is empty

## queue test ##


[x]Can successfully enqueue into a queue

[x] Can successfully enqueue multiple values into a queue

[x]Can successfully dequeue out of a queue the expected value

[x]Can successfully peek into a queue, seeing the expected value

[x]Can successfully empty a queue after multiple dequeues

[x]Can successfully instantiate an empty queue

[x]Calling dequeue or peek on empty queue raises exception



## code challenge 11

[]Create a new class called pseudo queue.

[]Do not use an existing Queue.

[]Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below),

[]Internally, utilize 2 Stack instances to create and manage the queue

## Methods:
[]enqueue Arguments: value Inserts value into the PseudoQueue, using a first-in, first-out approach.

enqueue(value)
Input	                       Args	                                              Output
[10]->[15]->[20]            	5	                                        [5]->[10]->[15]->[20]


[] dequeue Arguments: none Extracts a value from the PseudoQueue, using a first-in, first-out approach.h

Input	                           Output	                  Internal State
[5]->[10]->[15]->[20]	             20	                      [5]->[10]->[15])

 
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

## API
<!-- Description of each method publicly available to your Stack and Queue-->






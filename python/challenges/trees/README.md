# Trees
<!-- Short summary or background information -->

## Challenge
<!-- Description of the challenge -->

## node

[x]Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.


## Binary Tree
[x]Create a Binary Tree class

[x]Define a method for each of the depth first traversals:

[x]pre order

[x]in order

[x]post order which returns an array of the values, ordered appropriately.

[]Any exceptions or errors that come from your code should be semantic, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.


## Binary Search Tree

[x]Create a Binary Search Tree class

[x]This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following 

additional methods:

### Add

[x]Arguments: value

Return: nothing

Adds a new node with that value in the correct location in the binary search tree.

### Contains

[x]Argument: value

Returns: boolean indicating whether or not the value is in the tree at least once.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

pr_order() -> time: O(log(n)) -- space : O(n)
in_order() -> time: O(log(n)) -- space : O(n)
post_order() -> time: O(log(n)) -- space : O(n)
BFS() -> time: O(n) -- space : O(n)
add() -> time: O(n) -- space :O(1)
conatins() -> time: O(n) -- space :O(1)


## API
<!-- Description of each method publicly available in each of your trees -->



[usuful link](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-15/resources/Trees.html)





## class 16 



## Feature Tasks


[x]Write the following method for the Binary Tree class

[x]find maximum value

[x]Arguments: none

[x]Returns: number

[x]Find the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.

[x] write unit test

## Approach & Efficiency


![](/assets/tree_max.jpg)
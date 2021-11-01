## Breadth-first Traversal.

# Challenge Summary
<!-- Description of the challenge -->

Write a function called breadth first

Arguments: tree

Return: list of all values in the tree, in the order they were encountered

## Whiteboard Process
<!-- Embedded whiteboard image -->


![](https://github.com/ashrf288/data-structures-and-algorithms/blob/main/python/assets/breadth_first.png)



## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

## Solution
<!-- Show how to run your code, and examples of it in action -->

 A binary tree method which returns a list of items that it contains
    input: a binary search tree
    output: tree items in breadth order 

    create a stack and then enquque the tree head to the stack then create an empty list that will store
    the values by order 
    loop untill the stack is empty and  remove each elemnt from left to right 
    and then return the list 

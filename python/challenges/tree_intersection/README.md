
# Challenge Summary
<!-- Description of the challenge -->


Write a function called `tree_intersection` that takes two binary trees as parameters.

Using your Hashmap implementation as a part of your algorithm, return a set of values found in both trees.

## Whiteboard Process
<!-- Embedded whiteboard image -->

![](/python/assets/intersection.whitboard.jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
 BIG O

time---> o(n )

space---> o(n)


## Solution
<!-- Show how to run your code, and examples of it in action -->


it takes in a tree then travrse through it and then add each node data to a hash map then store the key in array (intersection) then takes the secound tree and travers through it and add each node to the same hash map then checks if the added node has the same key hash (index)  in intersection array if its true it add the value to a new array  (the data)
then return that array
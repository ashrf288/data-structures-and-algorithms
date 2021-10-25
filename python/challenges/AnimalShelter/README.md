# Challenge Summary
<!-- Description of the challenge -->

# First-in, First out Animal Shelter.


Create a class called AnimalShelter which holds only dogs and cats.

The shelter operates using a first-in, first-out approach.

Implement the following methods:

## 1-enqueue

Arguments: animal

animal can be either a dog or a cat object.

## 2-dequeue
[x]Arguments: pref

pref can be either "dog" or "cat"

Return: either a dog or a cat, based on preference.

If pref is not "dog" or "cat" then return null.


## [x] write unit teset

## Whiteboard Process
<!-- Embedded whiteboard image -->


![animal]()
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

## Solution
<!-- Show how to run your code, and examples of it in action -->


write class (animal) which will act as a node store data and refernce 

write class name (shelter) which will implemtt the stack 

enqueue works like reguler stack

the dequeu works by comparing the front of stack 
with the prefeernce if its match it will be removed from stack
but if its not then the front will be removed and re (queueu) to the stack
tail then compare the new front with preference untill it finds a match
# from challenges.linked_list.linked_list import (LinkedList,Node)
# # from pytest


# def test_node_has_int_data():
#     # Arrange any data that you need to run your test
#     expected = 1

#     # Act on the subject of the test to produce some actual output
#     node = Node(1)
#     actual = node.data

#     # Assert
#     assert actual == expected

# def test_node_has_str_data():
#     # Arrange any data that you need to run your test
#     expected = "a"

#     # Act on the subject of the test to produce some actual output
#     node = Node("a")
#     actual = node.data

#     # Assert
#     assert actual == expected


# def test_node_is_a_Node():
#     # Arrange any data that you need to run your test
#     expected = "Node"

#     # Act on the subject of the test to produce some actual output
#     node = Node(1)
#     actual = type(node).__name__

#     # Assert
#     assert actual == expected

# # def test_node_without_value():
# #     with pytest.raises(TypeError):
# #          Node()




# def test_new_linked_list_is_empty():
#   expected = None

#   ll = LinkedList()
#   actual = ll.head

#   assert actual == expected

# def test_linked_list_insert():
#   # Arrange
#   expected = 1
#   ll = LinkedList()

#   # Act
#   ll.insert(1)
#   node = ll.head
#   actual = node.data

#   # Assert
#   assert actual == expected

# def test_linked_list_insert_twice():
#   # Arrange
#   expected = 0
#   ll = LinkedList()

#   # Act
#   ll.insert(1)
#   ll.insert(0)
#   node = ll.head
#   actual = node.data

#   # Assert
#   assert actual == expected
#   assert ll.head.next.data == 1


# def test_includes():
    
#     ll=LinkedList()
#     ll.insert(1)
#     ll.insert(0)

#     ##
#     expected=True
#     actuall=ll.includes(1)
#     assert actuall==expected


# def test_str():
#     ll=LinkedList()
#     ll.insert(1)
#     ll.insert(0)

#      #output
#     expected= "{ 0 } -> { 1 } -> NULL"
#     actul= str(ll)

#     assert expected==actul
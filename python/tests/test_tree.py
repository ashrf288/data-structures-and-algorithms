from challenges.trees.trees import Binary_tree,Node




def test_first():
      # Create tree instance
  tree = Binary_tree()

  # Create Nodes for 1,2,3,4
  a_node = Node('a')
  b_node = Node('b')
  c_node = Node('c')
  d_node = Node('d')
  a_node.left = b_node
  a_node.right = c_node
  b_node.left = d_node

  # Add Root node to tree
  tree.root=a_node 
  
  # set expected list
  expected = ["a", "b", "d", "c"]
  # set actual to return value of post_order call
  actual = tree.pre_order()
  # assert actual is same as expected
  assert actual == expected
  print("test_post_order_ passed")  
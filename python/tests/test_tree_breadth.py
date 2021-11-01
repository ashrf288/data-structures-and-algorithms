from challenges.tree_breadth_first.tree_breadth import (breadth_first,Node,Binary_search_tree)



def test_breadth_first():
    #input
    tree=Binary_search_tree()
    a_node = Node('A')
    b_node = Node('B')
    c_node = Node('C')
    d_node = Node('D')
    e_node = Node('E')
    f_node = Node('F')
    g_node = Node('G')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    b_node.right = e_node
    c_node.left = f_node
    c_node.right = g_node
    tree.root=a_node
    #output
    expected=['A', 'B', 'C', 'D', 'E', 'F', 'G']
    actul=breadth_first(tree)

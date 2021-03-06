#!/usr/bin/env python3

import unittest
from binary_search_tree import Tree , InorderIterator, InorderIterator1, TreeNode

def insert(tree, lst):
    for elem in lst:
        tree.insert(elem)


t = unittest.TestCase()

# pre_order testcases
lst = [100,50,200,25,125,350]
tree = Tree()
insert(tree, lst)
t.assertEqual([100,50,25,200,125,350], tree.pre_order())   

lst = [100]
tree = Tree()
insert(tree, lst)
t.assertEqual([100], tree.pre_order())

lst = []
tree = Tree()
insert(tree, lst)
t.assertEqual([], tree.pre_order())

lst = [1,2,3,4,5,6,7,8]
tree = Tree()
insert(tree, lst)
t.assertEqual([1,2,3,4,5,6,7,8], tree.pre_order())

lst = [8,7,6,5,4,3,2,1]
tree = Tree()
insert(tree, lst)
t.assertEqual([8,7,6,5,4,3,2,1], tree.pre_order())

# are_identical testcases
lst1 = [8,7,6,5,4,3,2,1]
tree1 = Tree()
insert(tree1, lst1)

lst2 = [100,50,200,25,125,350]
tree2 = Tree()
insert(tree2, lst2)

t.assertEqual(False, Tree.are_identical(tree1.root, tree2.root))

lst1 = [100,50,200,25,125,350]
tree1 = Tree()
insert(tree1, lst1)

lst2 = [100,50,200,25,125,350]
tree2 = Tree()
insert(tree2, lst2)

t.assertEqual(True, Tree.are_identical(tree1.root, tree2.root))


lst1 = []
tree1 = Tree()
insert(tree1, lst1)

lst2 = []
tree2 = Tree()
insert(tree2, lst2)

t.assertEqual(True, Tree.are_identical(tree1.root, tree2.root))

lst1 = []
tree1 = Tree()
insert(tree1, lst1)

lst2 = [1]
tree2 = Tree()
insert(tree2, lst2)

t.assertEqual(False, Tree.are_identical(tree1.root, tree2.root))

lst1 = [100,50,200,25,125,350]
tree1 = Tree()
insert(tree1, lst1)

lst2 = [100,50,200,25,125,351]
tree2 = Tree()
insert(tree2, lst2)

t.assertEqual(False, Tree.are_identical(tree1.root, tree2.root))


lst1 = [100,50,200,25,125,350]
tree1 = Tree()
insert(tree1, lst1)

lst2 = [100,50,201,25,125,350]
tree2 = Tree()
insert(tree2, lst2)

t.assertEqual(False, Tree.are_identical(tree1.root, tree2.root))

# InorderIterator test cases

lst = [100,50,200,25,125,350]
tree = Tree()
insert(tree, lst)
it = InorderIterator(tree.root)
inorder = []
while it.hasNext():
    inorder.append(it.getNext())
t.assertEqual(inorder, [25, 50, 100, 125, 200, 350])


lst = []
tree = Tree()
insert(tree, lst)
t.assertRaises(Exception, InorderIterator, tree.root) # version 1
#version 2
with t.assertRaises(Exception) as cm:
    InorderIterator(tree.root)
t.assertEqual(cm.exception.args, ('Iteration not possible on empty tree',))

lst = [100]
tree = Tree()
insert(tree, lst)
it = InorderIterator(tree.root)
inorder = []
while it.hasNext():
    inorder.append(it.getNext())
t.assertEqual(inorder, [100])


lst = [100, 200, 300, 400, 500]
tree = Tree()
insert(tree, lst)
it = InorderIterator(tree.root)
inorder = []
while it.hasNext():
    inorder.append(it.getNext())
t.assertEqual(inorder, [100, 200, 300, 400, 500])



lst = [100, 90, 80, 70, 60, 50]
tree = Tree()
insert(tree, lst)
it = InorderIterator(tree.root)
inorder = []
while it.hasNext():
    inorder.append(it.getNext())
t.assertEqual(inorder, [50, 60, 70, 80, 90, 100])
# to make sure tree is not modified first time around
it = InorderIterator(tree.root)
inorder = []
while it.hasNext():
    inorder.append(it.getNext())
t.assertEqual(inorder, [50, 60, 70, 80, 90, 100])


# InorderIterator1 test cases

lst = [100,50,200,25,125,350]
tree = Tree()
insert(tree, lst)
it = InorderIterator1(tree.root)
inorder = []
while it.hasNext():
    inorder.append(it.getNext())
t.assertEqual(inorder, [25, 50, 100, 125, 200, 350])

lst = []
tree = Tree()
insert(tree, lst)
t.assertRaises(Exception, InorderIterator1, tree.root) # version 1
#version 2
with t.assertRaises(Exception) as cm:
    InorderIterator1(tree.root)
t.assertEqual(cm.exception.args, ('Iteration not possible on empty tree',))

lst = [100]
tree = Tree()
insert(tree, lst)
it = InorderIterator1(tree.root)
inorder = []
while it.hasNext():
    inorder.append(it.getNext())
t.assertEqual(inorder, [100])

lst = [100, 200, 300, 400, 500]
tree = Tree()
insert(tree, lst)
it = InorderIterator1(tree.root)
inorder = []
while it.hasNext():
    inorder.append(it.getNext())
t.assertEqual(inorder, [100, 200, 300, 400, 500])

lst = [100, 90, 80, 70, 60, 50]
tree = Tree()
insert(tree, lst)
it = InorderIterator1(tree.root)
inorder = []
while it.hasNext():
    inorder.append(it.getNext())
t.assertEqual(inorder, [50, 60, 70, 80, 90, 100])
# to make sure tree is not modified first time around
it = InorderIterator1(tree.root)
inorder = []
while it.hasNext():
    inorder.append(it.getNext())
t.assertEqual(inorder, [50, 60, 70, 80, 90, 100])

# inorder_iterative test cases

lst = [100,50,200,25,125,350]
tree = Tree()
insert(tree, lst)
inorder = tree.inorder_iterative()
t.assertEqual(inorder, [25, 50, 100, 125, 200, 350])
# to make sure tree is not modified by inorder_iterative
inorder = tree.inorder_iterative()
t.assertEqual(inorder, [25, 50, 100, 125, 200, 350])

lst = []
tree = Tree()
insert(tree, lst)
inorder = tree.inorder_iterative()
t.assertEqual(inorder, [])
# to make sure tree is not modified by inorder_iterative
inorder = tree.inorder_iterative()
t.assertEqual(inorder, [])


lst = [100]
tree = Tree()
insert(tree, lst)
inorder = tree.inorder_iterative()
t.assertEqual(inorder, [100])
# to make sure tree is not modified by inorder_iterative
inorder = tree.inorder_iterative()
t.assertEqual(inorder, [100])


lst = [100, 200, 300, 400, 500]
tree = Tree()
insert(tree, lst)
inorder = tree.inorder_iterative()
t.assertEqual(inorder, [100, 200, 300, 400, 500])
# to make sure tree is not modified by inorder_iterative
inorder = tree.inorder_iterative()
t.assertEqual(inorder, [100, 200, 300, 400, 500])


lst = [100, 90, 80, 70, 60, 50]
tree = Tree()
insert(tree, lst)
inorder = tree.inorder_iterative()
t.assertEqual(inorder, [50, 60, 70, 80, 90, 100])
# to make sure tree is not modified by inorder_iterative
inorder = tree.inorder_iterative()
t.assertEqual(inorder, [50, 60, 70, 80, 90, 100])


# Test inorder_successor
lst = [100,50,75,200,25,125,350]
tree = Tree()
insert(tree, lst)
# [25, 50, 75, 100, 125, 200, 350]
t.assertAlmostEqual(None, tree.inorder_successor(20))
t.assertAlmostEqual(50, tree.inorder_successor(25))
t.assertAlmostEqual(None, tree.inorder_successor(30))
t.assertAlmostEqual(75, tree.inorder_successor(50))
t.assertAlmostEqual(None, tree.inorder_successor(55))
t.assertAlmostEqual(100, tree.inorder_successor(75))
t.assertAlmostEqual(None, tree.inorder_successor(90))
t.assertAlmostEqual(125, tree.inorder_successor(100))
t.assertAlmostEqual(None, tree.inorder_successor(110))
t.assertAlmostEqual(200, tree.inorder_successor(125))
t.assertAlmostEqual(None, tree.inorder_successor(130))
t.assertAlmostEqual(350, tree.inorder_successor(200))
t.assertAlmostEqual(None, tree.inorder_successor(210))
t.assertAlmostEqual(None, tree.inorder_successor(350))
t.assertAlmostEqual(None, tree.inorder_successor(400))


lst =  [100, 200, 300, 400, 500]
tree = Tree()
insert(tree, lst)
# [100, 200, 300, 400, 500]]
t.assertAlmostEqual(None, tree.inorder_successor(20))
t.assertAlmostEqual(200, tree.inorder_successor(100))
t.assertAlmostEqual(None, tree.inorder_successor(110))
t.assertAlmostEqual(300, tree.inorder_successor(200))
t.assertAlmostEqual(None, tree.inorder_successor(210))
t.assertAlmostEqual(400, tree.inorder_successor(300))
t.assertAlmostEqual(None, tree.inorder_successor(310))
t.assertAlmostEqual(500, tree.inorder_successor(400))
t.assertAlmostEqual(None, tree.inorder_successor(410))
t.assertAlmostEqual(None, tree.inorder_successor(500))
t.assertAlmostEqual(None, tree.inorder_successor(510))


lst = [100, 90, 80, 70, 60, 50]
tree = Tree()
insert(tree, lst)
# [50, 60, 70, 80, 90, 100]
t.assertAlmostEqual(None, tree.inorder_successor(20))
t.assertAlmostEqual(60, tree.inorder_successor(50))
t.assertAlmostEqual(None, tree.inorder_successor(55))
t.assertAlmostEqual(70, tree.inorder_successor(60))
t.assertAlmostEqual(None, tree.inorder_successor(65))
t.assertAlmostEqual(80, tree.inorder_successor(70))
t.assertAlmostEqual(None, tree.inorder_successor(85))
t.assertAlmostEqual(100, tree.inorder_successor(90))
t.assertAlmostEqual(None, tree.inorder_successor(95))
t.assertAlmostEqual(None, tree.inorder_successor(100))
t.assertAlmostEqual(None, tree.inorder_successor(110))

tree = Tree()
tree.search(50)

node100 = TreeNode(100)
node50 = TreeNode(50)
node200 = TreeNode(200)
node25 = TreeNode(25)
node125 = TreeNode(125)
node350 = TreeNode(350)

node50.left = node25
node200.left = node125
node200.right = node350
node100.left = node50
node100.right = node200
tree.root = node100
t.assertEqual(id(node100), id(tree.search(100)))
t.assertEqual(id(node50), id(tree.search(50)))
t.assertEqual(id(node200), id(tree.search(200)))
t.assertEqual(id(node25), id(tree.search(25)))
t.assertEqual(id(node125), id(tree.search(125)))
t.assertEqual(id(node350), id(tree.search(350)))

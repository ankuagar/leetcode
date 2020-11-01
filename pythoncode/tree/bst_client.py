#!/usr/bin/env python3

import unittest
from binary_search_tree import Tree , InorderIterator, InorderIterator1

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


# inorder_iterative test cases

lst = [100,50,200,25,125,350]
tree = Tree()
insert(tree, lst)
inorder = tree.inorder_iterative()
t.assertEqual(inorder, [25, 50, 100, 125, 200, 350])

lst = []
tree = Tree()
insert(tree, lst)
inorder = tree.inorder_iterative()
t.assertEqual(inorder, [])


lst = [100]
tree = Tree()
insert(tree, lst)
inorder = tree.inorder_iterative()
t.assertEqual(inorder, [100])

lst = [100, 200, 300, 400, 500]
tree = Tree()
insert(tree, lst)
inorder = tree.inorder_iterative()
t.assertEqual(inorder, [100, 200, 300, 400, 500])


lst = [100, 90, 80, 70, 60, 50]
tree = Tree()
insert(tree, lst)
inorder = tree.inorder_iterative()
t.assertEqual(inorder, [50, 60, 70, 80, 90, 100])

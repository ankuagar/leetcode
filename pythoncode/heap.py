#!/usr/bin/env python3
import unittest

class Heap(object):
    '''
    Min Heap. Every root node is <= child nodes
    Uses 1 based indexing
    '''
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = []

    def size(self):
        return len(self.arr)

    def push(self, ele):
        if self.size() < self.capacity:
            self.arr.append(ele) # append new element to the end
            if self.size() > 1:
                self._heap_up() # and heap up
        else:
            raise Exception("Heap is full cannot push")
    
    def pop(self):
        if self.size() == 0:
            raise Exception("Heap is empty cannot pop")
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0] # swap the root with the last element
        ele = self.arr.pop() # pop the last element to get root
        if self.size() > 1:
            self._heap_down() # and heap down
        return ele

    def _heap_down(self):
        def _find_min_child_idx(parentidx):
            childidx0 = 2*parentidx
            childidx1 = 2*parentidx + 1
            if childidx1 > self.size():
                if childidx0 > self.size():
                    return None
                else:
                    return childidx0
            elif self.arr[childidx0 - 1] > self.arr[childidx1 - 1]:
                return childidx1
            else:
                return childidx0
        parentidx = 1
        min_child_idx = _find_min_child_idx(parentidx)
        while True:
            if self.arr[parentidx - 1] > self.arr[min_child_idx - 1]:
               self.arr[parentidx - 1], self.arr[min_child_idx - 1] = self.arr[min_child_idx - 1], self.arr[parentidx - 1]
               parentidx = min_child_idx
               min_child_idx = _find_min_child_idx(parentidx)
               if min_child_idx is None:
                   return
            else:
                return
        
    def _heap_up(self):
        childidx = self.size()
        parentidx = childidx//2
        while True:
            if self.arr[parentidx - 1] > self.arr[childidx - 1]: # if parent > child, then swap
                self.arr[childidx - 1], self.arr[parentidx - 1] = self.arr[parentidx - 1], self.arr[childidx - 1]
            if parentidx == 1: # if already at root
                return
            childidx = parentidx
            parentidx = childidx // 2

    def print_heap(self):
        '''
        Not so ugly level order traversal of the heap
        '''
        if not self.size() > 0:
            return
        parent = [1] # contains indexes
        temp = []
        while len(parent) > 0:
            temp.clear()
            for idx in parent:
                print(self.arr[idx-1], end=' ')
                temp.append(2*idx)
                temp.append(2*idx+1)
            parent = list(filter(lambda x: x <= self.size(),temp))
            print()
    
t = unittest.TestCase()
obj = Heap(4) # capacity is 4
t.assertEqual(0, obj.size())
t.assertEqual([], obj.arr)

obj.push(8)
t.assertEqual(1, obj.size())
t.assertEqual([8], obj.arr)

obj.push(4)
t.assertEqual(2, obj.size())
t.assertEqual([4,8], obj.arr)

obj.push(3)
t.assertEqual(3, obj.size())
t.assertEqual([3,8,4], obj.arr)

obj.push(5)
t.assertEqual(4, obj.size())
t.assertEqual([3,5,4,8], obj.arr)

with t.assertRaises(Exception): # push() to a heap that exceeds capacity should raise an exception
    obj.push(10)


t.assertEqual(obj.pop(), 3)
t.assertEqual(3, obj.size())
t.assertEqual([4,5,8], obj.arr)

t.assertEqual(obj.pop(), 4)
t.assertEqual(2, obj.size())
t.assertEqual([5,8], obj.arr)

t.assertEqual(obj.pop(), 5)
t.assertEqual(1, obj.size())
t.assertEqual([8], obj.arr)

t.assertEqual(obj.pop(), 8)
t.assertEqual(0, obj.size())
t.assertEqual([], obj.arr)


with t.assertRaises(Exception): # pop() from an empty heap should raise an exception
    obj.pop()

obj.push(5)
t.assertEqual(1, obj.size())
t.assertEqual([5], obj.arr)

obj.push(5)
t.assertEqual(2, obj.size())
t.assertEqual([5,5], obj.arr)

obj.push(5)
t.assertEqual(3, obj.size())
t.assertEqual([5,5,5], obj.arr)

obj.push(5)
t.assertEqual(4, obj.size())
t.assertEqual([5,5,5,5], obj.arr)

with t.assertRaises(Exception): # push() to a heap that exceeds capacity should raise an exception
    obj.push(5)
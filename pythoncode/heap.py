#!/usr/bin/env python3
import functools
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
    

obj = Heap(10)
obj.print_heap()
print("--")
obj.push(8)
obj.print_heap()
print("--")
obj.push(4)
obj.print_heap()
print("--")
obj.push(3)
obj.print_heap()
print("--")
obj.push(5)
obj.print_heap()
print("--")
obj.pop()
obj.print_heap()
print("--")
obj.pop()
obj.print_heap()
print("--")
obj.pop()
obj.print_heap()
print("--")
obj.pop()
obj.print_heap()
print("--")


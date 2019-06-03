#!/usr/bin/env python
from LinkedList import LinkedList

ll = LinkedList()
for i in range(10):
    ll.insert(i)
ll.print_list()
ll.reverse()
ll.print_list()

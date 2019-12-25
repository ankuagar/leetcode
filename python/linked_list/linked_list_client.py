#!/usr/bin/env python
from LinkedList import LinkedList

ll = LinkedList()
for i in range(10):
    ll.insert(i)
ll.print_list()
# ll.reverse()
# ll.print_list()
# ll.reverse1()
# reversed_list = ll.reverse2()
# reversed_list.print_list()

ll.reverse1()
ll.print_list()

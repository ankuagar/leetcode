#!/usr/bin/env python3
from LinkedList import LinkedList

# ll = LinkedList()
# for i in range(10):
#     ll.insert(i)
# ll.print_list()
# ll.reverse()
# ll.print_list()
# ll.reverse1()
# reversed_list = ll.reverse2()
# reversed_list.print_list()

# ll.reverse1()
# ll.print_list()

# ll.swap_nth_node(1)
# ll.print_list()
# ll.swap_nth_node(2)
# ll.print_list()
# ll.swap_nth_node(3)
# ll.print_list()
# ll.swap_nth_node(4)
# ll.print_list()
# ll.swap_nth_node(5)
# ll.print_list()
# ll.swap_nth_node(6)
# ll.print_list()
# ll.swap_nth_node(7)
# ll.print_list()
# ll.swap_nth_node(8)
# ll.print_list()
# ll.swap_nth_node(9)
# ll.print_list()
# ll.swap_nth_node(10)
# ll.print_list()

# ll1 = LinkedList()
# for i in range(10):
#     ll1.insert(i)
# ll1.reverse1()
# ll1.print_list()

# ll2 = LinkedList()
# for i in range(10,15,1):
#     ll2.insert(i)
# ll2.reverse1()
# ll2.print_list()

# ll3 = LinkedList.merge_sorted(ll1, ll2)
# ll3.print_list()


ll1 = LinkedList()
for i in [4, 8, 15, 19, 22]:
    ll1.insert(i)
ll1.reverse1()
ll1.print_list()

ll2 = LinkedList()
for i in [7, 9, 10, 16]:
    ll2.insert(i)
ll2.reverse1()
ll2.print_list()

ll3 = LinkedList.merge_sorted(ll1, ll2)
ll3.print_list()
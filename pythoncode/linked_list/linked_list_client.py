#!/usr/bin/env python3
from LinkedList import LinkedList
from unittest import TestCase

t = TestCase()

def test_reverse():
    ll = LinkedList()
    for i in range(10):
        ll.insert(i)
    t.assertEqual(str(ll), '9->8->7->6->5->4->3->2->1->0->')
    ll.reverse()
    t.assertEqual(str(ll), '0->1->2->3->4->5->6->7->8->9->')
    ll.reverse1()
    t.assertEqual(str(ll), '9->8->7->6->5->4->3->2->1->0->')
    t.assertEqual(str(ll.reverse2()), '0->1->2->3->4->5->6->7->8->9->')


def test_swap_node():
    def create_list():
        ll = LinkedList()
        for i in range(10):
            ll.insert(i)
        ll.reverse()
        return ll

    ll = create_list()
    ll.swap_nth_node(1)
    t.assertEqual(str(ll), '0->1->2->3->4->5->6->7->8->9->')

    ll = create_list()
    ll.swap_nth_node(2)
    t.assertEqual(str(ll), '1->0->2->3->4->5->6->7->8->9->')

    ll = create_list()
    ll.swap_nth_node(3)
    t.assertEqual(str(ll), '2->1->0->3->4->5->6->7->8->9->')

    ll = create_list()
    ll.swap_nth_node(4)
    t.assertEqual(str(ll), '3->1->2->0->4->5->6->7->8->9->')

    ll = create_list()
    ll.swap_nth_node(5)
    t.assertEqual(str(ll), '4->1->2->3->0->5->6->7->8->9->')

    ll = create_list()
    ll.swap_nth_node(6)
    t.assertEqual(str(ll), '5->1->2->3->4->0->6->7->8->9->')

    ll = create_list()
    ll.swap_nth_node(7)
    t.assertEqual(str(ll), '6->1->2->3->4->5->0->7->8->9->')

    ll = create_list()
    ll.swap_nth_node(8)
    t.assertEqual(str(ll), '7->1->2->3->4->5->6->0->8->9->')

    ll = create_list()
    ll.swap_nth_node(9)
    t.assertEqual(str(ll), '8->1->2->3->4->5->6->7->0->9->')

    ll = create_list()
    ll.swap_nth_node(10)
    t.assertEqual(str(ll), '9->1->2->3->4->5->6->7->8->0->')

def test_merge_sorted1():
    ll1 = LinkedList()
    for i in [4, 8, 15, 19, 22]:
        ll1.insert(i)
    ll1.reverse1()
    t.assertEqual(str(ll1), '4->8->15->19->22->')

    ll2 = LinkedList()
    for i in [7, 9, 10, 16]:
        ll2.insert(i)
    ll2.reverse1()
    t.assertEqual(str(ll2), '7->9->10->16->')

    ll3 = LinkedList.merge_sorted(ll1, ll2)
    t.assertEqual(str(ll3), '4->7->8->9->10->15->16->19->22->')

def test_merge_sorted2():

    ll1 = LinkedList()
    for i in range(10):
        ll1.insert(i)
    ll1.reverse1()
    t.assertEqual(str(ll1), '0->1->2->3->4->5->6->7->8->9->')


    ll2 = LinkedList()
    for i in range(10, 15, 1):
        ll2.insert(i)
    ll2.reverse1()
    t.assertEqual(str(ll2), '10->11->12->13->14->')

    ll3 = LinkedList.merge_sorted(ll1, ll2)
    t.assertEqual(str(ll3), '0->1->2->3->4->5->6->7->8->9->10->11->12->13->14->')

def test_merge_sorted3():
    ll1 = LinkedList()
    for i in range(10):
        ll1.insert(i)
    ll1.reverse1()
    t.assertEqual(str(ll1), '0->1->2->3->4->5->6->7->8->9->')

    ll2 = LinkedList()
    for i in [1, 10, 15]:
        ll2.insert(i)
    ll2.reverse1()
    t.assertEqual(str(ll2), '1->10->15->')

    ll3 = LinkedList()
    ll3 = LinkedList.merge_sorted(ll1, ll2)
    t.assertEqual(str(ll3), '0->1->1->2->3->4->5->6->7->8->9->10->15->')


test_reverse()
test_swap_node()
test_merge_sorted1()
test_merge_sorted2()
test_merge_sorted3()

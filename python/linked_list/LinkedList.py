class LinkedList(object):
    """
    Inserts new Nodes at the beginning of the list
    """
    class Node(object):
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            self.head = LinkedList.Node(data)
        else:
            new_head = LinkedList.Node(data)
            new_head.next = self.head
            self.head = new_head

    def reverse(self):
        """
        Uses a stack to reverse the LinkedList
        """
        stack = []
        current = self.head
        # store LinkedList items in stack
        while current is not None:
            stack.append(current.data)
            current = current.next
        # Iterate over stack items and insert into list, thereby reversing the list
        current = self.head
        for i in stack[::-1]:
            current.data = i
            current = current.next

    def reverse1(self):
        """
        Reverses the list in place i.e. uses no extra space to reverse the list
        """
        reversed = None # contains Node sequence in reversed order
        while self.head is not None:
            current = self.head
            self.head = self.head.next
            current.next = reversed
            reversed = current
        self.head = reversed

    def reverse2(self):
        """
        Reverses the current list by iterating over it and inserting the elements in a new list.
        Returns the new reversed list object
        """
        current = self.head
        reversed_list = LinkedList()
        while current is not None:
            reversed_list.insert(current.data)
            current = current.next
        return reversed_list


    def print_list(self):
        current = self.head
        while current is not None:
            print(str(current.data) + '->', end ='')
            current = current.next
        print()

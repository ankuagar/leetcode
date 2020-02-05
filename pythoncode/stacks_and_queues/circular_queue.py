class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.capacity = k
        self.size = 0
        self.data = [None] * self.capacity
        self.head = self.tail = None
        
    def __repr__(self):
        return "<Size: {}, Data: {}, Head: {}, Tail: {}>".format(self.size, self.data, self.head, self.tail)

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.size == self.capacity:
            return False
        
        elif self.size == 0:
            self.head = self.tail = 0
            self.data[self.tail] = value
            
        else:
            self.tail = (self.tail + 1) % self.capacity
            self.data[self.tail] = value
            
        self.size += 1
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.size == 0:
            return False 
        
        elif self.size == 1:
            self.data[self.head] = None # or self.data[self.tail] = None
            self.head = self.tail = None
            
        else:
            self.data[self.head] = None
            self.head = (self.head + 1) % self.capacity
        
        self.size -= 1
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.size == 0:
            return -1
        return self.data[self.head]
        

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.size == 0:
            return -1
        return self.data[self.tail]
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.size == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
l = [1,2,3]
obj = MyCircularQueue(5)

param_1 = obj.enQueue(8)
print repr(obj)
param_1 = obj.enQueue(9)
print repr(obj)
param_1 = obj.enQueue(10)
print repr(obj)
param_1 = obj.deQueue()
print repr(obj)
param_1 = obj.enQueue(10)
print repr(obj)
param_1 = obj.enQueue(10)
print repr(obj)

param_1 = obj.enQueue(11)
print repr(obj)
param_1 = obj.deQueue()
print repr(obj)
param_1 = obj.enQueue(12)
print repr(obj)
param_1 = obj.enQueue(15)
print repr(obj)

#param_1 = obj.enQueue(8)
#print repr(obj)
#param_1 = obj.enQueue(9)
#print repr(obj)
#param_1 = obj.enQueue(10)
#print repr(obj)
#param_1 = obj.enQueue(11)
#print repr(obj)
#param_1 = obj.enQueue(12)
#print repr(obj)

#param_1 = obj.deQueue()
#print repr(obj)

#param_1 = obj.deQueue()
#print repr(obj)

#param_1 = obj.deQueue()
#print repr(obj)

#param_1 = obj.deQueue()
#print repr(obj)

#param_1 = obj.deQueue()
#print repr(obj)

#param_1 = obj.enQueue(8)
#print repr(obj)

#param_1 = obj.enQueue(9)
#print repr(obj)

#param_1 = obj.enQueue(10)
#print repr(obj)

#param_1 = obj.enQueue(11)
#print repr(obj)

#param_1 = obj.enQueue(12)
#print repr(obj)


#param_2 = obj.deQueue()
#param_3 = obj.Front()
#param_4 = obj.Rear()
#param_5 = obj.isEmpty()
#param_6 = obj.isFull()

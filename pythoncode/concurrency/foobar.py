#!/usr/bin/env python
import threading 
from threading import Condition

def printFoo():
    print "foo",

def printBar():
    print "bar",

    
class FooBar(object):
    def __init__(self, n):
        self.c = Condition()
        self.foo_printed = False 
        self.n = n


    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        for i in xrange(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            self.c.acquire()
            printFoo()
            self.foo_printed = True
            self.c.notify()
            self.c.release()


    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for i in xrange(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            self.c.acquire()
            while not self.foo_printed:
                self.c.wait()
            printBar()
            self.foo_printed = False
            self.c.release()
            
obj = FooBar(2)
t1 = threading.Thread(target=obj.foo, name='thread1', args=(printFoo,)) # create thread with a target
t2 = threading.Thread(target=obj.bar, name='thread2', args=(printBar,)) # create thread with a target
t1.start()
t2.start()

t1.join()
t2.join()

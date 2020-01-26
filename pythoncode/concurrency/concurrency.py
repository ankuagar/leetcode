class Foo(object):
    def __init__(self):
        self.first_called = False
        self.second_called = False



    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_called = True


    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        while not self.first_called:
            pass
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.second_called = True
            
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        while not self.second_called:
            pass        
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        
        
from threading import Lock
class Foo(object):
    def __init__(self):
        self.lock1 = Lock()
        self.lock1.acquire()
        self.lock2 = Lock()
        self.lock2.acquire()

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lock1.release()

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        self.lock1.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.lock1.release()
        self.lock2.release()
            
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        self.lock2.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.lock2.release()


from threading import Event

class Foo(object):
    def __init__(self):
        self.e1 = Event()
        self.e1.clear() # internal flag set to false 
        self.e2 = Event()
        self.e2.clear() # internal flag set to false 


    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.e1.set()


    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        self.e1.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.e2.set()
            
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        self.e2.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()        



from threading import Condition

class Foo(object):
    def __init__(self):
        self.c1 = Condition()
        self.first_printed = False 
        self.c2 = Condition()
        self.second_printed = False 

        

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        # printFirst() outputs "first". Do not change or remove this line.
        self.c1.acquire()
        printFirst()
        self.first_printed = True
        self.c1.notify()
        self.c1.release()



    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        # printSecond() outputs "second". Do not change or remove this line.
        self.c1.acquire()
        while not self.first_printed:
            self.c1.wait()
        self.c1.release()
        self.c2.acquire()
        printSecond()
        self.second_printed = True
        self.c2.notify()
        self.c2.release()
            
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        # printThird() outputs "third". Do not change or remove this line.
        self.c2.acquire()
        while not self.second_printed:
            self.c2.wait()
        printThird()
        self.c2.release()
        
        
from threading import Semaphore 
class Foo(object):
    def __init__(self):
        self.s1 = Semaphore(1)
        self.s1.acquire()
        self.s2 = Semaphore(1)
        self.s2.acquire()


    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.s1.release()


    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        self.s1.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.s1.release()
        self.s2.release()
            
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        self.s2.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.s2.release()        
        
from threading import Semaphore 
class Foo(object):
    def __init__(self):
        self.s1 = Semaphore(0)        
        self.s2 = Semaphore(0)
        


    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.s1.release()


    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        self.s1.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.s2.release()
            
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        self.s2.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()        
        
        
from threading import Semaphore 
class FooBar(object):
    def __init__(self, n):
        self.foo_sem = Semaphore(0)
        self.bar_sem = Semaphore(1)
        self.n = n


    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        for i in xrange(self.n):
            self.bar_sem.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.foo_sem.release()


    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for i in xrange(self.n):
            self.foo_sem.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.bar_sem.release()        

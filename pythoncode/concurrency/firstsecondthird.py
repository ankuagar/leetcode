import threading
from threading import Condition, Lock, RLock

class Foo(object):
    def __init__(self):
        self.c1 = Condition()
        self.first_printed = False 
        self.c2 = Condition()
        self.second_printed = False 
        

    def first(self):
        """
        :type printFirst: method
        :rtype: void
        """
        self.c1.acquire()
        # printFirst() outputs "first". Do not change or remove this line.
        print "first",
        self.first_printed = True
        self.c1.notify()
        self.c1.release()


    def second(self):
        """
        :type printSecond: method
        :rtype: void
        """
        self.c1.acquire()
        while not self.first_printed:
            c1.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        self.c1.release()
        self.c2.acquire()
        print "second",
        self.second_printed = True
        self.c2.notify()
        self.c2.release()

#            
#            
    def third(self):
        """
        :type printThird: method
        :rtype: void
        """
        self.c2.acquire()
        while not self.second_printed:
            c2.wait()
        # printThird() outputs "third". Do not change or remove this line.
        print "third",
        #self.c2.release()
        
        
obj = Foo()
t1 = threading.Thread(target=obj.first, name='thread1') # create thread with a target
t2 = threading.Thread(target=obj.second, name='thread2') # create thread with a target         
t3 = threading.Thread(target=obj.third, name='thread3') # create thread with a target
t1.start()
t2.start()
t3.start()





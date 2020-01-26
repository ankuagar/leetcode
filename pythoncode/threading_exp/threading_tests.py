#!/usr/bin/env python

import threading
import time 

from threading import Thread, Timer, Lock, Semaphore, BoundedSemaphore, Condition
from random import randint

args = (1,2,3)
kwargs = {'a': 'b', 'c': 'd'}
var = 0
lock = Lock()
semaphore = BoundedSemaphore(5) # 5 threads can acquire at any given time
cv = Condition()


def simple_thread_target():
    global cv
    while True:
        time.sleep(5)
        print threading.active_count(), threading.enumerate()   
#        print cv.acquire(), "from thread1"
        
    print "I am a thread target"

"""
def thread_target(*args, **kwargs):
    time.sleep(randint(2,10))
    global var
    while not lock.acquire():
        print threading.current_thread(), " could not acquire lock, retrying after 1 second"
        time.sleep(1)
    print "----------------------------"
    print threading.current_thread(), " was able to acquire lock"        
    var += 1
#    print "I am a thread target:", args, kwargs
    print threading.current_thread(), " var is: ", var
    print "----------------------------"
    
    lock.release()

def thread_target_semaphore(*args, **kwargs):
    global var, semaphore
    time.sleep(randint(2,10))
    semaphore.acquire()
    #print threading.current_thread(), " could not acquire lock, retrying after 1 second"
    time.sleep(1)
    print "----------------------------"
    print threading.current_thread(), " was able to acquire lock"        
    var += 1
    print threading.current_thread(), " var is: ", var
    print "----------------------------"
    semaphore.release()
    semaphore.release()

"""    
""" 
# Example 1
class MyThread(Thread):
    def __init__(self, group, target, name, args, kwargs):
        super(MyThread, self).__init__(group, target, name, args, kwargs)
        
    def run(self):
        print threading.current_thread(), " in run method", self.isDaemon()
        time.sleep(20)

    
t = MyThread(None, thread_target, "thread-name",None, None) # create new thread, note: thread_target is not called
t.start()

print threading.current_thread(), " ", "starting wait", threading.current_thread().isDaemon() # main thread wait start
t.join(.5)
print threading.current_thread(), " ", "waiting done" # main thread wait done 


#Example 2
def clock(interval):
    while True:
        print "The time is %s" % time.ctime()
        time.sleep(interval)

t = threading.Thread(target=clock, args=(15,)) # create thread with a target 
t.daemon=False
t.start()

# Example 3
t = Timer(5, thread_target, args, kwargs)
t.start() # start the timer, wait for 5 seconds
time.sleep(1) # sleep for 1 second 
t.cancel() # cancel the timer


#Example 4
for i in xrange(1,11,1): # 1 through 10
    t = threading.Thread(target=thread_target_semaphore, name='thread' + str(i), args=args, kwargs=kwargs) # create thread with a target 
    t.start()
"""
#print cv.acquire(), "from main thread"
t = threading.Thread(target=simple_thread_target, name='thread1') # create thread with a target 
t.start()
#time.sleep(5)
#cv.release()

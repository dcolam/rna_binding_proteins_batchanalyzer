'''
Created on Apr 5, 2017

@author: david
'''
#!/usr/bin/python

import Queue
import threading
import time
from rbp_webdriver import rbp_batch


def thread_webdriver(dict_geneGroups):
    
    exitFlag = 0

    class myThread (threading.Thread):
        def __init__(self, threadID, name, q):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.q = q
        def run(self):
            print "Starting " + self.name
            process_data(self.name, self.q)
            print "Exiting " + self.name
    
    def process_data(threadName, q):
        while not exitFlag:
            queueLock.acquire()
            if not workQueue.empty():
                data = q.get()
                queueLock.release()
                print "%s processing %s" % (threadName, data[1])
                rbp_batch(data[0], data[1])
            else:
                queueLock.release()
            time.sleep(1)
    
    
    
    threadList = []
    for i in range(0, len(dict_geneGroups)):
        threadList.append('Thread-' + str(i))
    #nameList = ["One", "Two", "Three", "Four", "Five"]
    
    queueLock = threading.Lock()
    workQueue = Queue.Queue(10)
    threads = []
    threadID = 1
    
    # Create new threads
    for tName in threadList:
        thread = myThread(threadID, tName, workQueue)
        thread.start()
        threads.append(thread)
        threadID += 1
    
    # Fill the queue
    queueLock.acquire()
    for key in dict_geneGroups:
        workQueue.put([dict_geneGroups[key], key])
    queueLock.release()
    
    # Wait for queue to empty
    while not workQueue.empty():
        pass
    
    # Notify threads it's time to exit
    exitFlag = 1
    
    # Wait for all threads to complete
    for t in threads:
        t.join()
    print "Exiting Main Thread"

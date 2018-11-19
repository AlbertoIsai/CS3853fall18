#!/usr/bin/python

import sys

##fh = open(sys.argv[1], "r")
##for line in fh:
##    fields = line.strip().split()
##    print(fields[2])
##fh.close()





class Queue:
    def __init__(self):
        self.queue = list()
        self.maxSize = 16
        self.head = 0
        self.tail = 0

    #adding elements to queue
    def enqueue(self,data):
        #checking to avoid duplicate entry
        if data not in self.queue:
            self.queue.insert(0,data)
            return True
        self.queue.append(data)
        self.tail += 1
        return False
    
    #removing the last elemenet
    def dequeue(self):
        if self.size() <= 0:
            self.resetQueue()
            return("Queue Empty")
        data = self.queue[self.head]
        self.head+=1
        return data
    
    def size(self):
        return self.tail - self.head

    #reset queue
    def printQueue(self):
        self.tail = 0
        self.head = 0
        self.queue = list()


q = Queue()
hit = 0.00
miss = 0.00
total = 0.00
missRate = 0.00


fh = open(sys.argv[1], "r")

for line in fh:
    fields = line.strip().split()
 ##   print(fields[1],fields[2])
    if q.enqueue(fields[2]) is True:
        hit += 1
        print hit
    else:
        miss += 1
        print miss
 ##   print(q.size())

total = hit + miss
print miss
print total
missRate = (miss / total) * 1.0

print float(missRate)

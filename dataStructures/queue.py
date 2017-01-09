#!/usr/bin/env python

class Queue:
    """ simple queue implementation using default list """

    def __init__(self, list=None):
        if list == None:
            list = []
        self.list = list

    def enqueue(self, elem):
        self.list.append(elem)

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty !')
        else:
            result = self.list[0]
            self.list.pop(0)
            return result

    def is_empty(self):
        if self.list:
            return False
        else:
            return True

    def peek(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        else:
            return self.list[0]

    def size(self):
        if self.list:
            return len(self.list)
        else:
            return 0
             
    def show(self):
        print self.list


